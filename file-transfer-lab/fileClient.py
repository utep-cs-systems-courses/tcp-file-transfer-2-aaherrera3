import os, socket

address = "127.0.0.1"
port = 50001

clientSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create server socket
clientSock.connect((address,port)) # connect to server socket
clientSock.send(b"Hello World") # send Hello World
print(clientSock.recv(1024)) # reciving a mesage of 30 bytes