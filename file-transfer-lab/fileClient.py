import os, socket, tqdm, sys

address = "127.0.0.1" # ip address
port = 50001 # port number to connect to 
bufferSize = 4096 #number of bytes to send each time


clientSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create server socket

print(f"[+] Conneting to {address}:{port}")
clientSock.connect((address,port)) # connect to server socket
print(f"[+] Connected.")

try:
    fileName = input("File Transfer Name:")
    if "<exit>" in fileName:
        clientSock.close()
        sys.exit(1)
    fileSize = os.path.getsize(fileName) #size of file 
except FileNotFoundError:
    print("File not found.") # If file not found 
else:
    clientSock.send(f"{fileName}|{fileSize}".encode()) # Send file name and size
    
    progress = tqdm.tqdm(range(fileSize), f"Sending {fileName}", unit="B", unit_scale=True, unit_divisor=1024)

    with open(fileName, "rb") as f: #open file in byte reading, and using with to manage open file 
        for _ in progress:
            bytesRead = f.read(bufferSize) # read from file 4096 bytes
            if not bytesRead:
                break # File transfer Done
            clientSock.sendall(bytesRead) # Assure all info is send
            progress.update(len(bytesRead)) # update progress bar 

    clientSock.close()    


