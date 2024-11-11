from flask import Flask, request, jsonify, render_template, session
from PIL import Image
from io import BytesIO
import base64
import os
from dotenv import load_dotenv
import pandas as pd
#from multiprocessing import Lock, Manager
#from multiprocessing.managers import AcquirerProxy, BaseManager, DictProxy
import math
from jeopardy_data import get_jeopardy_clues, return_clue_and_response
from flask_sse import sse
import threading
import serial
import json
import time

ser = serial.Serial('/dev/ttyACM0', 9600)  # Replace '/dev/ttyACM0' with your actual serial port

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
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 86400  # Cache static files for 1 day (86400 seconds)

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


def serial_listener():
    while True:
        line = ser.readline().decode('utf-8').strip()
        if line == '6_press':
            print("Host button pressed", flush=True)
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
            print("Host button released", flush=True)
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
            print(f"Player {player_id} buzzed in", flush=True)
            with app.app_context():
                handle_player_buzz(player_id)


def handle_player_buzz(player_id):
    current_time = time.time()
    with shared_lock:
        # Check if player has already buzzed in incorrectly
        if player_id in shared_dict.get('buzzed_out_players', []):
            print(f"Player {player_id} has already buzzed out on this clue", flush=True)
            return  # Ignore the buzz
        # Check if buzzing is enabled
        print("Debug 1", flush=True)
        if shared_dict.get('buzzing_enabled', False):
            print("Debug 2", flush=True)
            # Check if the player is already locked out
            lockout_end = shared_dict.get('lockout_times', {}).get(player_id, 0)
            if current_time >= lockout_end:
                print("Debug 3", flush=True)
                # First player to buzz in
                if shared_dict.get('buzzed_in_player') is None:
                    print("Debug 4", flush=True)
                    shared_dict['buzzed_in_player'] = player_id
                    shared_dict['buzzing_enabled'] = False  # Disable further buzzing
                    print(f"Alerting client of player {player_id} buzz", flush=True)
                    sse.publish({'player': player_id}, type='button_press')
            else:
                # Player is locked out
                print(f"Player {player_id} locked out", flush=True)
                pass  # Ignore the buzz
        else:
            # Buzzing is not enabled (reading phase or after first buzz)
            # Apply early buzz-in penalty if host is still holding the button
            ##if shared_dict.get('host_button_pressed', False):
            # Lock out the player for 0.25 seconds from now
            print(f"Locking out player {player_id} for 0.25 seconds", flush=True)
            shared_dict.setdefault('lockout_times', {})[player_id] = current_time + 0.25 #TODO: Thorough testing
            print(f"Player {player_id} locked out until {current_time + 0.25}")


# @app.after_request
# def add_header(response):
#     if request.path.startswith('/static/'):
#         # For static files, cache for 1 day
#         response.headers['Cache-Control'] = 'public, max-age=86400'
#     else:
#         # For dynamic content, you may choose to disable caching
#         response.headers['Cache-Control'] = 'no-store'
#     return response

@app.route('/host_decision', methods=['POST'])
def host_decision():
    data = request.get_json()
    player_id = data['player_id']
    is_correct = data['is_correct']
    clue_value = data['value']
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
            else:
                # No remaining players, close the clue
                shared_dict['buzzing_enabled'] = False
                sse.publish({'action': 'close_clue'}, type='clue_closed')
            # Prepare data for SSE
            score_update_data = {
                'player_id': player_id,
                'new_score': shared_dict['scores'][player_id],
                'scores': shared_dict['scores']
            }
            # Broadcast the score update
            sse.publish(score_update_data, type='score_update')
            return jsonify({'message': 'Score updated, player incorrect'})



@app.route('/')
def title_screen_h():
    return render_template('title_screen_h.html')

@app.route('/write_name_h')
def write_name_h():
    return render_template('write_name_h.html')

@app.route('/select_difficulty_h')
def select_difficulty_h():
    return render_template('select_difficulty_h.html')

#TODO: if using this assistant method approach, either use shared_lock or get both windows to share the same flask session
@app.route('/select-difficulty')
def select_difficulty():
    difficulty = request.args.get('level', 'Easy')
    # Store the difficulty in the session or process as needed
    session['difficulty'] = difficulty
    print(f"Difficulty selected: {difficulty}", flush=True)  # For debugging
    return jsonify({'message': f'Difficulty set to {difficulty}'})

@app.route('/main_board_p')
def main_board_p():
    with shared_lock:
        categories = shared_dict['categories']
        enabled_buttons = shared_dict['enabled_buttons']
        scores = shared_dict['scores']
    # Convert to regular list for logging
    enabled_buttons_list = [list(row) for row in enabled_buttons]
    app.logger.debug(f"Enabled buttons: {enabled_buttons_list}")
    cache_buster = int(time.time())  # Use the current timestamp
    return render_template('main_board_p.html', categories=categories, enabled_buttons=enabled_buttons_list, scores=scores, cache_buster=cache_buster)

@app.route('/main_board_h')
def main_board_h():
    with shared_lock:
        categories = shared_dict['categories']
        enabled_buttons = shared_dict['enabled_buttons']
        scores = shared_dict['scores']
    # Convert to regular list for logging
    enabled_buttons_list = [list(row) for row in enabled_buttons]
    app.logger.debug(f"Enabled buttons: {enabled_buttons_list}")
    cache_buster = int(time.time())  # Use the current timestamp
    return render_template('main_board_h.html', categories=categories, enabled_buttons=enabled_buttons_list, scores=scores, cache_buster=cache_buster)


#TODO: Fix this hackiness. No need to have both the clue_p route and clue_h route go through the logic
# of getting the clue and response on their own. Can probably just have clue_h do it and share it with
# clue_p as long as it's quick enough or whatever.
@app.route('/clue_p')
def clue_p():
    row = request.args.get('row')
    col = request.args.get('col')

    with shared_lock:
        categories = shared_dict['categories']
        clues = shared_dict['clues']
        scores = shared_dict['scores']
    try:
        clue, response = return_clue_and_response(categories, clues, row, col)
    except ValueError as e:
        return str(e), 400
    cache_buster = int(time.time())
    return render_template('clue_h.html', clue=clue, response=response, scores=scores, cache_buster=cache_buster)



@app.route('/clue_h')
def clue_h():
    row = request.args.get('row')
    col = request.args.get('col')

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
    except ValueError as e:
        return str(e), 400
    cache_buster = int(time.time())
    return render_template('clue_h.html', clue=clue, response=response, scores=scores, cache_buster=cache_buster)




@app.route('/title_video_p')
def title_video_p():
    return render_template('title_video_p.html')

@app.route('/get-clues', methods=['GET'])
def get_clues():
    df_jeopardy_active_clues, _ = get_jeopardy_clues(proj_path)
    clues = df_jeopardy_active_clues.to_dict(orient='records')
    return jsonify(clues)

@app.route('/button-clicked', methods=['POST'])
def button_clicked():
    data = request.json
    row = int(data.get('row'))
    col = int(data.get('col'))
    with shared_lock:
        shared_dict['enabled_buttons'][row][col] = 0  # Disable the button
    app.logger.debug(f"Button at ({row}, {col}) set to 0")
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
    return jsonify({'message': 'Name saved successfully!'})


if __name__ == '__main__':
    # Start the serial listener thread
    serial_thread = threading.Thread(target=serial_listener)
    serial_thread.daemon = True  # Ensures thread exits when main program exits
    serial_thread.start()

    # If you run this with debug it starts a parent process and a child process, both of which
    # try to read the serial port which causes issues meaning the buttons won't work
    # correctly 100% of the time.
    #app.run(debug=True, port=5000)
    app.run(port=5000)