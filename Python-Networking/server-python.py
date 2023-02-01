import socket
import threading
import sys

# Variables to hold information about client connections
connections = []
total_connections = 0

# Client class, a new instance is created for each connected client
# Each instance has a socket and address associated with it,
# an assigned ID and a name chosen by the client
class Client(threading.Thread):
    def __init__(self, socket, address, id, name, signal):
        # Call the parent constructor to initialize the thread
        threading.Thread.__init__(self)
        self.socket = socket
        self.address = address
        self.id = id
        self.name = name
        self.signal = signal
    
    # Return a string representation of the client instance
    def __str__(self):
        return str(self.id) + " " + str(self.address)
    
    # Attempt to receive data from the client
    def run(self):
        while self.signal:
            try:
                # Receive data from the client socket
                data = self.socket.recv(32)
            except:
                # If there is an error, assume the client has disconnected
                print("Client " + str(self.address) + " has disconnected")
                self.signal = False
                # Remove the client from the connections list
                connections.remove(self)
                break
            if data != "":
                # If data is received, print it in the server and send it back to every
                # client aside from the client that sent it
                print("Person " + str(self.id) + ": " + str(data.decode("utf-8")))
                for client in connections:
                    if client.id != self.id:
                        # Send the received data to all connected clients except the sender
                        client.socket.sendall(data)

# Wait for new connections to the server
def newConnections(socket):
    while True:
        # Accept new connections from clients
        sock, address = socket.accept()
        global total_connections
        # Create a new Client instance for the new connection
        connections.append(Client(sock, address, total_connections, "Name", True))
        # Start the new client thread
        connections[len(connections) - 1].start()
        print("New connection at ID " + str(connections[len(connections) - 1]))
        # Increment the total number of connections
        total_connections += 1

def main():
    print("Linares Messenger Server")
    # Get the host and port from the user
    host = input("Host: ")
    port = int(input("Port: "))

    # Create a new server socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Bind the socket to the specified host and port
    sock.bind((host, port))
    # Start listening for incoming connections
    sock.listen(5)

    # Create a new thread to wait for new connections
    newConnectionsThread = threading.Thread(target = newConnections, args = (sock,))
    newConnectionsThread.start()
    

# Call the main function to start the program
main()
