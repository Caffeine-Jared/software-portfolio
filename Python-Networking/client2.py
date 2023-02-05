import socket
import random
from threading import Thread
from datetime import datetime
from colorama import Fore, init

# Initialize colors for text output
init()

# Define available colors for the client
available_colors = [
    Fore.RED,
    Fore.GREEN,
    Fore.YELLOW,
    Fore.BLUE,
    Fore.MAGENTA,
    Fore.CYAN,
    Fore.WHITE,
    Fore.LIGHTBLACK_EX,
    Fore.LIGHTRED_EX,
    Fore.LIGHTGREEN_EX,
    Fore.LIGHTYELLOW_EX,
    Fore.LIGHTBLUE_EX,
    Fore.LIGHTMAGENTA_EX,
    Fore.LIGHTCYAN_EX,
    Fore.LIGHTWHITE_EX
]

# Randomly choose a color for the client
client_color = random.choice(available_colors)

# Ask the user for the server's IP address
server_host = input("Enter the server's IP address: ")

# Ask the user for the server's port number
server_port = int(input("Enter the server's port number: "))

# Set the separator token
separator_token = "<SEP>" # Token to separate client name and message

# Initialize TCP socket for communication
client_socket = socket.socket()

# Connect to the server
print("[*] Connecting to {}:{}...".format(server_host, server_port))
client_socket.connect((server_host, server_port))
print(f"Connected to {server_host}.")

# Prompt the user for their name
client_name = input("Enter your name: ")

def listen_for_messages():
    # Function to listen for incoming messages from the server and print them.
    while True:
        message = client_socket.recv(1024).decode()
        print("\n" + message)

def start_listening_thread():
    # Create a new thread to listen for incoming messages and print them
    listen_thread = Thread(target=listen_for_messages)
    
    # Set the thread to be a daemon so it ends when the main thread ends
    listen_thread.daemon = True
    
    # Start the thread
    listen_thread.start()

start_listening_thread()

# Continuously prompt the user for a message to send to the server
def send_message(client_socket, client_name, client_color, separator_token):
    def send_message_func():
        while True:
            message_to_send =  input("Enter a message to send to the server (q to quit): ")
            if message_to_send.lower() == 'q':
                return

            current_date_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S') 
            message_to_send = f"{client_color}[{current_date_time}] {client_name}{separator_token}{message_to_send}{Fore.RESET}"
            client_socket.send(message_to_send.encode())
    return send_message_func

send_func = send_message(client_socket, client_name, client_color, separator_token)
send_func()
client_socket.close()