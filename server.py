import socket
import threading


server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('127.0.0.1',6969))
server.listen()

print("SERVER IS LISTENING !!!")

nicknames: list[str] = []
clients: list[socket.socket] = []

def broadcast(message): 
    for client in clients: 
        client.send(message.encode('ascii'))

def handle(client):
    while True: 
        message = client.recv(1024).decode()
        if message == "close" : 
            break
        broadcast(message)

def accept_clients(): 
    while True: 
        client, address = server.accept()
        clients.append(client)
        print(f"{address} connected to server.")
        client.send("NICK".encode('ascii'))
        name = client.recv(1024).decode()
        nicknames.append(name)

        print(f"{name} joined the server!!")

        thread = threading.Thread(target=handle,args=(client,))
        thread.start()

accept_clients()
