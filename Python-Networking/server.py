import socket
from threading import Thread

# IP address of the server
SERVER_IP_ADDRESS = "0.0.0.0"
SERVER_PORT_NUMBER = 8080 # port number to be used by the server
MESSAGE_SEPARATOR = "<SEP>" # token to separate client's name and message

# initialize a set to store all connected client's sockets
connected_client_sockets = set()

# create a TCP socket for the server
server_socket = socket.socket()

# set the port as reusable
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# bind the server socket to the specified IP address and port number
server_socket.bind((SERVER_IP_ADDRESS, SERVER_PORT_NUMBER))

# listen for incoming connections
server_socket.listen(5)
print(f"Server Details: {SERVER_IP_ADDRESS}:{SERVER_PORT_NUMBER}")

def listen_for_client_messages(client_socket):
    # This function listens for messages from a specified client socket. Whenever a message is received, it broadcasts the
    # message to all other connected clients. It runs on a separate thread for each connected client.

    while True:
        try:
            # receive message from the `client_socket`
            message = client_socket.recv(1024).decode()
        except Exception as e:
            # if an error occurs, it means the client is no longer connected
            # remove the client socket from the set of connected clients
            print(f"[!] Error: {e}")
            connected_client_sockets.remove(client_socket)
        else:
            # replace the MESSAGE_SEPARATOR token with ": " for better display
            message = message.replace(MESSAGE_SEPARATOR, ": ")
        # send the received message to all connected clients
        for other_client_socket in connected_client_sockets:
            other_client_socket.send(message.encode())

def accept_incoming_connections():
    while True:
        # continuously listen for incoming connections
        client_socket, client_address = server_socket.accept()
        print(f"[+] {client_address} connected.")
        # add the newly connected client socket to the set of connected clients
        connected_client_sockets.add(client_socket)
        # start a new thread to listen for messages from this client
        client_thread = Thread(target=listen_for_client_messages, args=(client_socket,))
        # set the thread as a daemon thread so it will end when the main thread ends
        client_thread.daemon = True
        # start the thread
        client_thread.start()

accept_incoming_connections()

