import os, socket, tqdm


address = "" #default ip for server 
port = 50001 # port number hosting
bufferSize = 4096 #number of bytes to send each time

serverSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create server socket
serverSock.bind((address,port)) # bind socket to port 50001 and let it chose the address 
serverSock.listen(1) # have the server socket in listen mode to 1 connection 

print(f"[+]Waiting for connection.")
convSock, clienAddress = serverSock.accept() #creation of connection scoket
print(f"[+] Connection to {clienAddress}.") 

fileInfo = convSock.recv(bufferSize).decode() # get file info 
fileName, fileSize = fileInfo.split("|") # split file info 

fileName = os.path.basename(fileName) # remove absolute path
fileSize = int(fileSize) # conver to int

progress = tqdm.tqdm(range(fileSize), f"Sending {fileName}", unit="B", unit_scale=True, unit_divisor=1024)
with open("(Server)"+fileName, "wb") as f:
    for _ in progress:
        bytesRead = convSock.recv(bufferSize) # recevive 4096 bytes from client
        if not bytesRead:
            print("File Transfer Complete")
            break #file transfer done
        f.write(bytesRead) # Write 4096 to server file
        progress.update(len(bytesRead)) # update progress bar 

convSock.close()
serverSock.close()
    


    

