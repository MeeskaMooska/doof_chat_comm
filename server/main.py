from flask_app import app
from socket_app import run_socket_server
import threading
import waitress

def run_flask():
    waitress.serve(app, host='0.0.0.0', port=8080)

def run_socket():
    run_socket_server()

if __name__ == '__main__':
    flask_thread = threading.Thread(target=run_flask)
    socket_thread = threading.Thread(target=run_socket)

    flask_thread.start()
    socket_thread.start()

    flask_thread.join()
    socket_thread.join()
