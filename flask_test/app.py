from flask import Flask, request, jsonify, render_template, session
from PIL import Image
from io import BytesIO
import base64
import os
from dotenv import load_dotenv
import pandas as pd
from multiprocessing import Lock
from multiprocessing.managers import AcquirerProxy, BaseManager, DictProxy
import math
from jeopardy_data import get_jeopardy_clues, return_clue_and_response

# Load environment variables from the .env file
load_dotenv()

# Access the PROJ_PATH environment variable
proj_path = os.getenv('PROJ_PATH')

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a strong secret key


# Set up shared state management
def get_shared_state(host, port, key):
    shared_dict = {}
    shared_lock = Lock()
    manager = BaseManager((host, port), key)
    manager.register("get_dict", lambda: shared_dict, DictProxy)
    manager.register("get_lock", lambda: shared_lock, AcquirerProxy)
    try:
        manager.get_server()
        manager.start()
    except OSError:  # Address already in use
        manager.connect()
    return manager.get_dict(), manager.get_lock()

HOST = "127.0.0.1"
PORT = 35791
KEY = b"secret"
shared_dict, shared_lock = get_shared_state(HOST, PORT, KEY)

# Clear shared state on startup to ensure random categories each time
with shared_lock:
    shared_dict.clear()  # Ensure we don't have the same values each time we run the app
    categories, clues = get_jeopardy_clues(proj_path)
    shared_dict['categories'] = categories
    shared_dict['clues'] = clues  # Store clues in shared_dict






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
    print(f"Difficulty selected: {difficulty}")  # For debugging
    return jsonify({'message': f'Difficulty set to {difficulty}'})

@app.route('/main_board_p')
def main_board_p():
    with shared_lock:
        categories = shared_dict['categories']
    return render_template('main_board_p.html', categories=categories)

@app.route('/main_board_h')
def main_board_h():
    with shared_lock:
        categories = shared_dict['categories']
    return render_template('main_board_h.html', categories=categories)

#TODO: Fix this hackiness. No need to have both the clue_p route and clue_h route go through the logic
# of getting the clue and response on their own. Can probably just have clue_h do it and share it with
# clue_p as long as it's quick enough or whatever.
@app.route('/clue_p')
def clue_p():
    button_name = request.args.get('name')
    with shared_lock:
        categories = shared_dict['categories']
        clues = shared_dict['clues']
    try:
        clue, response = return_clue_and_response(categories, clues, button_name)
    except ValueError as e:
        return str(e), 400
    return render_template('clue_p.html', clue=clue, response=response)



@app.route('/clue_h')
def clue_h():
    button_name = request.args.get('name')
    with shared_lock:
        categories = shared_dict['categories']
        clues = shared_dict['clues']
    try:
        clue, response = return_clue_and_response(categories, clues, button_name)
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

@app.route('/button-clicked', methods=['GET'])
def button_clicked():
    button_name = request.args.get('name')
    print(f'{button_name} clicked!')
    app.logger.info(f'{button_name} clicked!')
    return jsonify({'message': f'{button_name} clicked!'})

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
