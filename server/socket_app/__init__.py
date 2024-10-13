import socket

class SocketServer:
    def __init__(self):
        self.server_socket = None
        self.client_socket = None

    def update_server_socket(self, server_socket):
        self.server_socket = server_socket

    def update_client_socket(self, client_socket):
        self.client_socket = client_socket

socket_data = SocketServer()

def run_socket_server():
    # Create socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_data.update_server_socket(server_socket)

    port_num = 12500

    # Bind to localhost and port
    server_socket.bind(('0.0.0.0', port_num))

    # Listen for incoming connections (1 connection for simplicity)
    server_socket.listen(1)
    print(f"Socket server is listening on localhost:{port_num}")

    # Accept the client connection
    client_socket, addr = server_socket.accept()
    print(f"Connection established with {addr}")

    # Update the client socket in the socket_data object
    socket_data.update_client_socket(client_socket)

def send_message(message, document = None):
    if socket_data.client_socket:
        if document:
            # Send the document to the client
            socket_data.client_socket.send(document.encode('utf-8'))

            socket_data.client_socket.send(message.encode('utf-8'))

            # Receive message from the client
            response = socket_data.client_socket.recv(4090).decode('utf-8')

            return response
        
        else:
            socket_data.client_socket.send(message.encode('utf-8'))

            # Receive message from the client
            response = socket_data.client_socket.recv(4090).decode('utf-8')

            return response
    
    else:
        print("We're sorry, but the server is not connected to a client socket.")

# Kill server and client sockets
def kill_sockets():
    if socket_data.client_socket:
        socket_data.client_socket.send("Server is shutting down.".encode('utf-8'))
        socket_data.client_socket.close()
    
    if socket_data.server_socket:
        socket_data.server_socket.close()
        print("Server socket closed.")