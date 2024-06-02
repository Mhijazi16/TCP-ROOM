import socket
import threading

# Create a socket object for the server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the server to localhost and port 6969
server.bind(('127.0.0.1', 6969))

# Listen for incoming connections
server.listen()

# Print a message indicating that the server is listening
print("SERVER IS LISTENING !!!")

# List to store client nicknames and their socket objects
nicknames: list[str] = []
clients: list[socket.socket] = []

# Function to broadcast messages to all connected clients
def broadcast(message):
    for client in clients:
        client.send(message.encode('ascii'))

# Function to handle individual client connections
def handle(client):
    while True:
        # Receive message from client
        message = client.recv(1024).decode()
        # If client sends "close", break the loop to close the connection
        if message == "close":
            break
        # Broadcast the received message to all clients
        broadcast(message)

# Function to accept incoming client connections
def accept_clients():
    while True:
        # Accept client connection
        client, address = server.accept()
        # Add client to list of clients
        clients.append(client)
        # Print connection message
        print(f"{address} connected to server.")
        # Request client's nickname
        client.send("NICK".encode('ascii'))
        # Receive and store client's nickname
        name = client.recv(1024).decode()
        nicknames.append(name)

        print(f"{name} joined the server!!")

        # Start a new thread to handle the client
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

# Start accepting client connections
accept_clients()
