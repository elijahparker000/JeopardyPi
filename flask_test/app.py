from flask import Flask, request, jsonify, render_template
from PIL import Image
from io import BytesIO
import base64
import os
from dotenv import load_dotenv
import pandas as pd
from multiprocessing import Lock
from multiprocessing.managers import AcquirerProxy, BaseManager, DictProxy

# Load environment variables from the .env file
load_dotenv()

# Access the PROJ_PATH environment variable
proj_path = os.getenv('PROJ_PATH')

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a strong secret key

# Define the function to get Jeopardy clues
def get_jeopardy_clues():
    file_path = os.path.join(proj_path, "clues/jeopardy.csv")
    df = pd.read_csv(file_path)
    df.columns = df.columns.str.strip()
    show_round_category = df[['Show Number', 'Round', 'Category']]
    df_show_list = show_round_category.drop_duplicates()
    df_jeopardy = df_show_list[df_show_list['Round'] == 'Jeopardy!']
    df_jeopardy_sampled = df_jeopardy.sample(n=6)
    df_jeopardy_active_clues = pd.merge(df, df_jeopardy_sampled, on=['Show Number', 'Round', 'Category'], how='inner')
    categories = df_jeopardy_sampled['Category'].tolist()  # Get the categories
    return df_jeopardy_active_clues, categories

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
    shared_dict.clear() #this ensures we don't have the same values each time we run the app
    _, categories = get_jeopardy_clues()
    shared_dict['categories'] = categories

@app.route('/')
def title_screen_h():
    return render_template('title_screen_h.html')

@app.route('/write_name_h')
def write_name_h():
    return render_template('write_name_h.html')

@app.route('/main_board_p')
def main_board_p():
    with shared_lock:
        categories = shared_dict['categories']
    return render_template('main_board_p.html', categories=categories)

@app.route('/clue_p')
def clue_p():
    return render_template('clue_p.html')

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
