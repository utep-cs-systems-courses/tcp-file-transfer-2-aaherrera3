import os, socket

address = ""
port = 50001

serverSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create server socket
serverSock.bind((address,port)) # bind socket to port 50001 and let it chose the address 
serverSock.listen(1) # have the server socket in listen mode to 1 connection 

convSock, clienAddress = serverSock.accept() #creation of connection scoket

message = convSock.recv(30) # reciving a mesage of 30 bytes
print(message) # print message
convSock.send(message) # send message back 
