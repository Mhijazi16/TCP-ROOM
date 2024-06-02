import socket
import threading

# Create a socket object for the client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the client to the server using localhost and port 6969
client.connect(('127.0.0.1', 6969))

# Get the user's name
name = input("ENTER NAME: ")

# Function to send messages to the server
def send():
    while True:
        # Get input from the user
        val = input("")
        # If user inputs "close", send it to the server to close the connection
        if val == "close":
            client.send(val.encode('ascii'))
        # Prepare message with user's name and send it to the server
        message = f"[{name}]: {val}"
        client.send(message.encode('ascii'))

# Function to receive messages from the server
def receive():
    while True:
        # Receive message from the server
        message = client.recv(1024).decode()
        # If server requests user's name, send it
        if message == "NICK":
            client.send(name.encode('ascii'))
        # Print the received message
        print(message)

# Create two threads for sending and receiving messages concurrently
send_thread = threading.Thread(target=send)
receive_thread = threading.Thread(target=receive)

# Start both threads
send_thread.start()
receive_thread.start()
