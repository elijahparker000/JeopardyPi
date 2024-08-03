# app.py
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('proper_scaling_demo.html')

@app.route('/second')
def second():
    return render_template('second.html')

@app.route('/button-clicked', methods=['GET'])
def button_clicked():
    button_name = request.args.get('name')
    print(f'{button_name} clicked!')
    app.logger.info(f'{button_name} clicked!')
    return jsonify({'message': f'{button_name} clicked!', 'redirect': '/second'})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
