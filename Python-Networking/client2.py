import socket
import threading
import sys

# Function to wait for incoming data from the server and print it
def receive(socket, signal):
    while signal:
        try:
            # Receive data from the server with a buffer size of 32
            data = socket.recv(32)
            # Decode the incoming message from bytes to a string and print it
            print(str(data.decode("utf-8")))
        except:
            # If there is an error in receiving the message, print a disconnection message and break the loop
            print("You have been disconnected from the server")
            signal = False
            break

# Prompt the user to enter the host and port values
host = input("Host: ")
port = int(input("Port: "))

# Attempt to connect to the server
try:
    # Create a socket object
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connect to the server with the host and port values
    sock.connect((host, port))
except:
    # If the connection cannot be established, print an error message and exit the program with a status code of 0
    print("Could not make a connection to the server")
    input("Press enter to quit")
    sys.exit(0)

# Create a new thread for the receive function
receiveThread = threading.Thread(target = receive, args = (sock, True))
# Start the receive thread
receiveThread.start()

# Continuously wait for the user's input and send it to the server
def send_message(sock):
    while True:
        # Get the message from the user
        message = input("Enter a message: ")
        # Encode the message as bytes and send it to the server
        sock.sendall(str.encode(message))
send_message(sock)
