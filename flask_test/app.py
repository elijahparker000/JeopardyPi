# app.py
from flask import Flask, request, jsonify, render_template, session
from PIL import Image
from io import BytesIO
import base64
import os
from dotenv import load_dotenv
import pandas as pd

# Load environment variables from the .env file
load_dotenv()

# Access the PROJ_PATH environment variable
proj_path = os.getenv('PROJ_PATH')

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a strong secret key TODO: Figure out what this means

# Define the function to get Jeopardy clues
def get_jeopardy_clues():
    file_path = os.path.join(proj_path, "clues/jeopardy.csv")
    df = pd.read_csv(file_path)
    df.columns = df.columns.str.strip()
    show_round_category = df[['Show Number', 'Round', 'Category']]
    df_show_list = show_round_category.drop_duplicates()
    df_jeopardy = df_show_list[df_show_list['Round'] == 'Jeopardy!']
    #df_jeopardy_sampled = df_jeopardy.sample(n=6, random_state=42) # pulls the same every time for testing
    df_jeopardy_sampled = df_jeopardy.sample(n=6)
    df_jeopardy_active_clues = pd.merge(df, df_jeopardy_sampled, on=['Show Number', 'Round', 'Category'], how='inner')
    categories = df_jeopardy_sampled['Category'].tolist()  # Get the categories
    return df_jeopardy_active_clues, categories

@app.route('/')
def index():
    return render_template('title_screen.html')

@app.route('/write_name')
def next_page():
    return render_template('write_name.html')

@app.route('/main_board_p')
def main_board():
    if 'categories' not in session:
        _, categories = get_jeopardy_clues()
        session['categories'] = categories
    return render_template('main_board_p.html', categories=session['categories'])

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
