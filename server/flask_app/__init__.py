from flask import Flask, request, jsonify
from flask_app.config import Config
from socket_app import send_message
import socket

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/process_request', methods=['GET'])
def index():
    message = request.args.get('message')
    document = request.args.get('document')

    # User attatched a pdf file
    if document:
        model_response = send_message(message, document)
    
    else:
        model_response = send_message(message)

    return jsonify({'response': model_response})
