# app.py
from flask import Flask, request, jsonify, render_template
from PIL import Image
from io import BytesIO
import base64
import os
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Access the PROJ_PATH environment variable
proj_path = os.getenv('PROJ_PATH')


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('title_screen.html')

@app.route('/write_name')
def next_page():
    return render_template('write_name.html')

@app.route('/main_board_p')
def main_board():
    return render_template('main_board_p.html')




@app.route('/button-clicked', methods=['GET'])
def button_clicked():
    button_name = request.args.get('name')
    print(f'{button_name} clicked!')
    app.logger.info(f'{button_name} clicked!')
    return jsonify({'message': f'{button_name} clicked!'})#, 'redirect': '/second'})

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
