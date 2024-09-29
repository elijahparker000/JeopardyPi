from flask import Flask, request, jsonify, render_template, session
from PIL import Image
from io import BytesIO
import base64
import os
from dotenv import load_dotenv
import pandas as pd
from multiprocessing import Lock, Manager
from multiprocessing.managers import AcquirerProxy, BaseManager, DictProxy
import math
from jeopardy_data import get_jeopardy_clues, return_clue_and_response

# Load environment variables from the .env file
load_dotenv()

# Access the PROJ_PATH environment variable
proj_path = os.getenv('PROJ_PATH')

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a strong secret key

# Set the maximum age (in seconds) for caching static files
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 86400  # Cache static files for 1 day (86400 seconds)

HOST = "127.0.0.1"
PORT = 35791
KEY = b"secret"
# shared_dict, shared_lock = get_shared_state(HOST, PORT, KEY)

# Set up shared state management
manager = Manager()
shared_dict = manager.dict()
shared_lock = manager.Lock()

# Initialize shared state
with shared_lock:
    shared_dict.clear()  # Ensure we don't have the same values each time we run the app
    categories, clues = get_jeopardy_clues(proj_path)
    shared_dict['categories'] = categories
    shared_dict['clues'] = clues  # Store clues in shared_dict
    # Initialize enabled_buttons as a managed list of managed lists
    shared_dict['enabled_buttons'] = manager.list(
        [manager.list([1] * 6) for _ in range(5)]
    )




@app.after_request
def add_header(response):
    if request.path.startswith('/static/'):
        # For static files, cache for 1 day
        response.headers['Cache-Control'] = 'public, max-age=86400'
    else:
        # For dynamic content, you may choose to disable caching
        response.headers['Cache-Control'] = 'no-store'
    return response

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
    # Convert to regular list for logging
    enabled_buttons_list = [list(row) for row in enabled_buttons]
    app.logger.debug(f"Enabled buttons: {enabled_buttons_list}")
    return render_template('main_board_p.html', categories=categories, enabled_buttons=enabled_buttons_list)


@app.route('/main_board_h')
def main_board_h():
    with shared_lock:
        categories = shared_dict['categories']
        enabled_buttons = shared_dict['enabled_buttons']
    # Convert to regular list for logging
    enabled_buttons_list = [list(row) for row in enabled_buttons]
    app.logger.debug(f"Enabled buttons: {enabled_buttons_list}")
    return render_template('main_board_h.html', categories=categories, enabled_buttons=enabled_buttons_list)


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
    try:
        clue, response = return_clue_and_response(categories, clues, row, col)
    except ValueError as e:
        return str(e), 400
    return render_template('clue_p.html', clue=clue, response=response)



@app.route('/clue_h')
def clue_h():
    row = request.args.get('row')
    col = request.args.get('col')

    with shared_lock:
        categories = shared_dict['categories']
        clues = shared_dict['clues']
    try:
        clue, response = return_clue_and_response(categories, clues, row, col)
    except ValueError as e:
        return str(e), 400
    return render_template('clue_h.html', clue=clue, response=response)




@app.route('/title_video_p')
def title_video_p():
    return render_template('title_video_p.html')

@app.route('/get-clues', methods=['GET'])
def get_clues():
    df_jeopardy_active_clues, _ = get_jeopardy_clues()
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
    app.run(debug=True, port=5000)
