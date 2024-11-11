from flask import Flask, request, jsonify, render_template, session
from PIL import Image
from io import BytesIO
import base64
import os
from dotenv import load_dotenv
import pandas as pd
import math
from jeopardy_data import get_jeopardy_clues, return_clue_and_response
from flask_sse import sse
import threading
import serial
import json
import time

import logging
from logging.handlers import RotatingFileHandler

# Set up logging
logger = logging.getLogger('jeopardy_app')
logger.setLevel(logging.DEBUG)

# Create handlers
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

file_handler = RotatingFileHandler('jeopardy_app.log', maxBytes=1_000_000, backupCount=5)
file_handler.setLevel(logging.INFO)

# Create formatters and add them to the handlers
console_formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(console_formatter)

file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)

# Add handlers to the logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)

ser = serial.Serial('/dev/ttyACM0', 9600)  # Replace with your actual serial port

# Load environment variables from the .env file
load_dotenv()

# Access the PROJ_PATH environment variable
proj_path = os.getenv('PROJ_PATH')

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a strong secret key

# Configure Flask-SSE
app.config["REDIS_URL"] = "redis://localhost:6379"
app.register_blueprint(sse, url_prefix='/stream')

# Set the maximum age (in seconds) for caching static files
#TODO: This could be useful for speeding up rendering in the final product? Not sure.
#app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 86400  # Cache static files for 1 day

# Set up shared state management
shared_lock = threading.Lock()
shared_dict = {}

# Initialize shared state
with shared_lock:
    shared_dict.clear()  # Ensure we don't have the same values each time we run the app
    categories, clues = get_jeopardy_clues(proj_path)
    shared_dict['categories'] = categories
    shared_dict['clues'] = clues  # Store clues in shared_dict
    # Initialize enabled_buttons as a list of lists
    shared_dict['enabled_buttons'] = [[1] * 6 for _ in range(5)]
    # Initialize player scores
    shared_dict['scores'] = {str(i): 0 for i in range(1, 6)}  # Player IDs '1' to '5'
    shared_dict['buzzed_in_player'] = None
    shared_dict['buzzed_out_players'] = []
    shared_dict['buzzing_enabled'] = False
    shared_dict['host_button_pressed'] = False
    shared_dict['lockout_times'] = {}
    shared_dict['answering_window_ended'] = False
    # Log the categories
    logger.info("Categories for the game:")
    for idx, category_name in enumerate(categories, start=1):
        logger.info(f"Category {idx}: {category_name}")
    # Log the clues and responses
    logger.info("Clues and Responses loaded for the game:")
    for category_name, category_clues in clues.items():
        for clue_idx, clue_info in enumerate(category_clues, start=1):
            clue_text = clue_info.get('clue')
            response = clue_info.get('response')
            # Assuming the clue values are $200, $400, $600, etc.
            value = clue_idx * 200
            logger.info(f"Category: '{category_name}', Value: ${value}, Clue: '{clue_text}', Response: '{response}'")
logger.info('Shared state initialized')

def serial_listener():
    while True:
        line = ser.readline().decode('utf-8').strip()
        if line == '6_press':
            logger.info("Host button pressed")
            with app.app_context():
                with shared_lock:
                    if shared_dict.get('buzzing_enabled', False):
                        # Host pressed button during buzzing phase
                        shared_dict['buzzing_enabled'] = False
                        shared_dict['answering_window_ended'] = True
                        # Remove indicators and play timeout sound
                        sse.publish({'action': 'buzzing_ended'}, type='clue_control')
                    else:
                        # Host pressed button during reading phase
                        shared_dict['host_button_pressed'] = True
                        sse.publish({'action': 'show_clue'}, type='clue_control')
        elif line == '6_release':
            logger.info("Host button released")
            with app.app_context():
                with shared_lock:
                    if shared_dict.get('answering_window_ended', False):
                        shared_dict['answering_window_ended'] = False
                        # Close the clue screen
                        sse.publish({'action': 'close_clue'}, type='clue_closed')
                    elif shared_dict.get('host_button_pressed', False):
                        shared_dict['host_button_pressed'] = False
                        shared_dict['buzzing_enabled'] = True
                        sse.publish({'action': 'enable_buzz'}, type='clue_control')
        elif line in {'1', '2', '3', '4', '5'}:
            player_id = line
            logger.info(f"Player {player_id} buzzed in")
            with app.app_context():
                handle_player_buzz(player_id)

def handle_player_buzz(player_id):
    current_time = time.time()
    with shared_lock:
        # Check if player has already buzzed in incorrectly
        if player_id in shared_dict.get('buzzed_out_players', []):
            logger.debug(f"Player {player_id} has already buzzed out on this clue")
            return  # Ignore the buzz
        # Check if buzzing is enabled
        if shared_dict.get('buzzing_enabled', False):
            # Check if the player is already locked out
            lockout_end = shared_dict.get('lockout_times', {}).get(player_id, 0)
            if current_time >= lockout_end:
                # First player to buzz in
                if shared_dict.get('buzzed_in_player') is None:
                    logger.debug(f"Player {player_id} is the first to buzz in")
                    shared_dict['buzzed_in_player'] = player_id
                    shared_dict['buzzing_enabled'] = False  # Disable further buzzing
                    logger.info(f"Alerting client of player {player_id} buzz")
                    sse.publish({'player': player_id}, type='button_press')
            else:
                # Player is locked out
                logger.debug(f"Player {player_id} is locked out until {lockout_end}")
                pass  # Ignore the buzz
        else:
            # Buzzing is not enabled (reading phase or after first buzz)
            # Apply early buzz-in penalty if host is still holding the button
            logger.debug(f"Buzzing not enabled, locking out player {player_id} for 0.25 seconds")
            shared_dict.setdefault('lockout_times', {})[player_id] = current_time + 0.25  # TODO: Thorough testing
            logger.debug(f"Player {player_id} locked out until {current_time + 0.25}")

@app.route('/host_decision', methods=['POST'])
def host_decision():
    data = request.get_json()
    player_id = data['player_id']
    is_correct = data['is_correct']
    clue_value = data['value']
    logger.info(f"Host decision received: Player {player_id}, is_correct: {is_correct}, clue_value: {clue_value}")
    with shared_lock:
        # Update the player's score
        if is_correct:
            score_delta = clue_value
            shared_dict['scores'][player_id] += score_delta
            # Reset game state
            shared_dict['buzzed_in_player'] = None
            shared_dict['buzzing_enabled'] = False
            shared_dict['buzzed_out_players'] = []
            # Prepare data for SSE
            score_update_data = {
                'player_id': player_id,
                'new_score': shared_dict['scores'][player_id],
                'scores': shared_dict['scores']
            }
            # Broadcast the score update
            sse.publish(score_update_data, type='score_update')
            # Close the clue screen
            sse.publish({'action': 'close_clue'}, type='clue_closed')
            logger.info(f"Player {player_id} answered correctly. Score updated.")
            return jsonify({'message': 'Score updated successfully and clue closed'})
        else:
            score_delta = -clue_value
            shared_dict['scores'][player_id] += score_delta
            # Add the player to buzzed out players
            shared_dict['buzzed_out_players'].append(player_id)
            # Reset buzzed_in_player
            shared_dict['buzzed_in_player'] = None
            # Check if any players are left who haven't buzzed in incorrectly
            remaining_players = set(['1', '2', '3', '4', '5']) - set(shared_dict['buzzed_out_players'])
            if remaining_players:
                shared_dict['buzzing_enabled'] = True  # Allow other players to buzz in
                logger.info(f"Player {player_id} answered incorrectly. Other players can buzz in.")
            else:
                # No remaining players, close the clue
                shared_dict['buzzing_enabled'] = False
                sse.publish({'action': 'close_clue'}, type='clue_closed')
                logger.info(f"Player {player_id} answered incorrectly. No remaining players. Clue closed.")
            # Prepare data for SSE
            score_update_data = {
                'player_id': player_id,
                'new_score': shared_dict['scores'][player_id],
                'scores': shared_dict['scores']
            }
            # Broadcast the score update
            sse.publish(score_update_data, type='score_update')
            return jsonify({'message': 'Score updated, player incorrect'})

@app.route('/log_client', methods=['POST'])
def log_client():
    data = request.get_json()
    level = data.get('level', 'INFO').upper()
    message = data.get('message', '')
    
    # Map level string to logging level
    level_mapping = {
        'DEBUG': logging.DEBUG,
        'INFO': logging.INFO,
        'WARNING': logging.WARNING,
        'ERROR': logging.ERROR,
        'CRITICAL': logging.CRITICAL
    }
    log_level = level_mapping.get(level, logging.INFO)
    
    # Log the message
    logger.log(log_level, f'CLIENT LOG - {message}')
    
    return '', 204  # No Content

@app.route('/')
def title_screen_h():
    logger.info("Title screen requested (host)")
    return render_template('title_screen_h.html')

@app.route('/write_name_h')
def write_name_h():
    logger.info("Write name screen requested (host)")
    return render_template('write_name_h.html')

@app.route('/select_difficulty_h')
def select_difficulty_h():
    logger.info("Select difficulty screen requested (host)")
    return render_template('select_difficulty_h.html')

@app.route('/select-difficulty')
def select_difficulty():
    difficulty = request.args.get('level', 'Easy')
    # Store the difficulty in the session or process as needed
    session['difficulty'] = difficulty
    logger.info(f"Difficulty selected: {difficulty}")
    return jsonify({'message': f'Difficulty set to {difficulty}'})

@app.route('/main_board_p')
def main_board_p():
    with shared_lock:
        categories = shared_dict['categories']
        enabled_buttons = shared_dict['enabled_buttons']
        scores = shared_dict['scores']
    # Convert to regular list for logging
    enabled_buttons_list = [list(row) for row in enabled_buttons]
    logger.debug(f"Enabled buttons (player): {enabled_buttons_list}")
    return render_template('main_board_p.html', categories=categories, enabled_buttons=enabled_buttons_list, scores=scores)

@app.route('/main_board_h')
def main_board_h():
    with shared_lock:
        categories = shared_dict['categories']
        enabled_buttons = shared_dict['enabled_buttons']
        scores = shared_dict['scores']
    # Convert to regular list for logging
    enabled_buttons_list = [list(row) for row in enabled_buttons]
    logger.debug(f"Enabled buttons (host): {enabled_buttons_list}")
    return render_template('main_board_h.html', categories=categories, enabled_buttons=enabled_buttons_list, scores=scores)

@app.route('/clue_p')
def clue_p():
    row = request.args.get('row')
    col = request.args.get('col')
    logger.info(f"Clue requested by player screen at row {row}, col {col}")
    with shared_lock:
        categories = shared_dict['categories']
        clues = shared_dict['clues']
        scores = shared_dict['scores']
    try:
        clue, response = return_clue_and_response(categories, clues, row, col)
        category = categories[int(col)]  # Get the category name
        logger.debug(f"Player screen displaying Clue: Category='{category}', Clue='{clue}'")
    except ValueError as e:
        logger.error(f"Error retrieving clue: {e}")
        return str(e), 400
    return render_template('clue_p.html', clue=clue, response=response, scores=scores)

@app.route('/clue_h')
def clue_h():
    row = request.args.get('row')
    col = request.args.get('col')
    logger.info(f"Clue requested by host screen at row {row}, col {col}")
    with shared_lock:
        categories = shared_dict['categories']
        clues = shared_dict['clues']
        scores = shared_dict['scores']
        # Reset game state
        shared_dict['buzzed_in_player'] = None
        shared_dict['buzzed_out_players'] = []
        shared_dict['buzzing_enabled'] = False
        shared_dict['host_button_pressed'] = False
        shared_dict['lockout_times'] = {}
    try:
        clue, response = return_clue_and_response(categories, clues, row, col)
        category = categories[int(col)]  # Get the category name
        logger.info(f"Selected Clue: Category='{category}', Clue='{clue}', Response='{response}'")
    except ValueError as e:
        logger.error(f"Error retrieving clue: {e}")
        return str(e), 400
    return render_template('clue_h.html', clue=clue, response=response, scores=scores)

@app.route('/title_video_p')
def title_video_p():
    logger.info("Title video requested (player)")
    return render_template('title_video_p.html')

@app.route('/get-clues', methods=['GET'])
def get_clues():
    df_jeopardy_active_clues, _ = get_jeopardy_clues(proj_path)
    clues = df_jeopardy_active_clues.to_dict(orient='records')
    logger.info("Clues requested")
    return jsonify(clues)

@app.route('/button-clicked', methods=['POST'])
def button_clicked():
    data = request.json
    row = int(data.get('row'))
    col = int(data.get('col'))
    with shared_lock:
        shared_dict['enabled_buttons'][row][col] = 0  # Disable the button
    logger.debug(f"Button at ({row}, {col}) clicked and disabled")
    return jsonify({'message': f'Button at ({row}, {col}) clicked!'})

@app.route('/save-name', methods=['POST'])
def save_name():
    data = request.json
    image_data = data['image'].split(',')[1]
    image = Image.open(BytesIO(base64.b64decode(image_data)))

    # Ensure the directory exists
    save_path = os.path.join(proj_path, "flask_test/static/images/names")
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    image.save(os.path.join(save_path, 'player_name.png'))
    logger.info("Player name image saved")
    return jsonify({'message': 'Name saved successfully!'})

if __name__ == '__main__':
    # Start the serial listener thread
    serial_thread = threading.Thread(target=serial_listener)
    serial_thread.daemon = True  # Ensures thread exits when main program exits
    serial_thread.start()

    logger.info("Starting Jeopardy application")
    # If you run this with debug it starts a parent process and a child process, both of which
    # try to read the serial port which causes issues meaning the buttons won't work
    # correctly 100% of the time.
    #app.run(debug=True, port=5000)
    app.run(port=5000)
