from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)

socketio = SocketIO(app)

@app.route('/message', methods = ['GET'])
def message():
    return render_template('index.html')

@socketio.on('message')
def handle_message(msg):
    socketio.emit('message', msg)

@socketio.on('connected')
def connected():
    print("Connected")

@socketio.on('disconnected')
def handle_disconnected():
    print('Disconnected')

socketio.run(app, debug=True)