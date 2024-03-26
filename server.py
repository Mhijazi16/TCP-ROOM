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
