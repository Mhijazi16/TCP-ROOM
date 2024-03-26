import socket
import threading

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('127.0.0.1',6969))

name = input("ENTER NAME :")

def send(): 
    while True:
        val = input("")
        if val == "close": 
            client.send(val.encode('ascii'))
        message = f"[{name}]: {val}"
        client.send(message.encode('ascii'))

def recive():
    while True: 
        message = client.recv(1024).decode()
        if message == "NICK": 
            client.send(name.encode('ascii'))
        print(message)
