from flask import Flask,render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY']="woo"
socket = SocketIO(app)
somelist = ['apple', 'banana', 'grapes', 'watermelon']
i=0

@app.route("/")
def main():
    return render_template("main.html")

@socket.on('message')
def handlemsg(msg):
    global i
    if i<len(somelist):
        socket.send(somelist[i])
        i+=1

if __name__ == "__main__":
    socket.run(app)