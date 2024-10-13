import socket
import os

SERVER_IP = os.environ.get('SERVER_IP')

def run_socket_client():
    # Create socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    client_socket.connect((SERVER_IP, 12500))
    print("Connected to the server.")

    while True:
        # Receive message from the server
        message = client_socket.recv(1024).decode('utf-8')

        print(message)
        
        client_socket.send("Sample response.".encode('utf-8'))

    # Close the connection
    client_socket.close()

if __name__ == '__main__':
    run_socket_client()
