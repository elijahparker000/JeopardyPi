from flask import Flask, request, jsonify, render_template
from PIL import Image
from io import BytesIO
import base64
import os
from dotenv import load_dotenv
import pandas as pd
from multiprocessing import Lock
from multiprocessing.managers import AcquirerProxy, BaseManager, DictProxy
import math

# Load environment variables from the .env file
load_dotenv()

# Access the PROJ_PATH environment variable
proj_path = os.getenv('PROJ_PATH')

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a strong secret key

# Define the function to get Jeopardy clues
# Define the function to get Jeopardy clues along with values, questions, and answers
def get_jeopardy_clues():
    file_path = os.path.join(proj_path, "clues/jeopardy.csv")
    df = pd.read_csv(file_path)
    df.columns = df.columns.str.strip()

    # Filter the DataFrame for the 'Jeopardy!' round and remove duplicates of categories
    show_round_category = df[['Show Number', 'Round', 'Category']]
    df_show_list = show_round_category.drop_duplicates()
    df_jeopardy = df_show_list[df_show_list['Round'] == 'Jeopardy!']

    # Randomly sample 6 categories
    df_jeopardy_sampled = df_jeopardy.sample(n=6)

    # Merge the sampled categories with the original dataframe to get the clues and answers
    df_jeopardy_active_clues = pd.merge(
        df, 
        df_jeopardy_sampled, 
        on=['Show Number', 'Round', 'Category'], 
        how='inner'
    )

    # Extract the categories, questions, answers, and values for the selected categories
    categories = df_jeopardy_sampled['Category'].tolist()  # List of selected categories

    # For each category, get the corresponding clues and answers
    clues = {}
    for category in categories:
        # Filter the DataFrame for the current category
        clues_for_category = df_jeopardy_active_clues[df_jeopardy_active_clues['Category'] == category]
        
        # Collect the clue value, question, and answer in a list of dictionaries
        clues[category] = [
            {
                'clue': clue['Question'],
                'response': clue['Answer']
            }
            for _, clue in clues_for_category.iterrows()
        ]

    return categories, clues


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
    categories, clues = get_jeopardy_clues()
    shared_dict['categories'] = categories
    shared_dict['clues'] = clues  # Store clues in shared_dict


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
    print(button_name, flush=True)

    # Parse the button name to extract the category and clue numbers
    try:
        parts = button_name.split()
        category_number = int(parts[1]) - 1  # Category number, adjust for 0-based indexing
        clue_number = int(parts[3]) - 1      # Clue number, adjust for 0-based indexing
    except (IndexError, ValueError):
        return "Invalid clue identifier", 400

    with shared_lock:
        categories = shared_dict['categories']  # List of categories
        clues = shared_dict['clues']  # Dictionary of clues by category

    # Retrieve the category name
    category_name = categories[category_number]

    # Retrieve the clues for the specified category
    category_clues = clues.get(category_name)

    # Retrieve the specific clue
    if clue_number >= len(category_clues):
        return "Invalid clue number", 400

    selected_clue = category_clues[clue_number]
    clue_text = selected_clue['clue']
    response_text = selected_clue['response']

    print(f"Selected clue: {clue_text}, Response: {response_text}", flush=True)

    # Store the selected clue in shared_dict for the player screen
    with shared_lock:
        shared_dict['current_clue'] = {
            'clue': clue_text,
            'response': response_text
        }

    # Pass the clue and response to the template
    return render_template('clue_p.html', clue=clue_text, response=response_text)



@app.route('/clue_h')
def clue_h():
    button_name = request.args.get('name')
    print(button_name, flush=True)

    # Parse the button name to extract the category and clue numbers
    try:
        parts = button_name.split()
        category_number = int(parts[1]) - 1  # Category number, adjust for 0-based indexing
        clue_number = int(parts[3]) - 1      # Clue number, adjust for 0-based indexing
    except (IndexError, ValueError):
        return "Invalid clue identifier", 400

    with shared_lock:
        categories = shared_dict['categories']  # List of categories
        clues = shared_dict['clues']  # Dictionary of clues by category

    # Retrieve the category name
    category_name = categories[category_number]

    # Retrieve the clues for the specified category
    category_clues = clues.get(category_name)

    # Retrieve the specific clue
    if clue_number >= len(category_clues):
        return "Invalid clue number", 400

    selected_clue = category_clues[clue_number]
    clue_text = selected_clue['clue']
    response_text = selected_clue['response']

    print(f"Selected clue: {clue_text}, Response: {response_text}", flush=True)

    # Store the selected clue in shared_dict for the player screen
    with shared_lock:
        shared_dict['current_clue'] = {
            'clue': clue_text,
            'response': response_text
        }

    # Pass the clue and response to the template
    return render_template('clue_h.html', clue=clue_text, response=response_text)




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
