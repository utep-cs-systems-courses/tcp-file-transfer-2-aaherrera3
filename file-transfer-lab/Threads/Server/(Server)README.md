# Transfer Lab
tcp transfer file 

Directory `file-transfer-lab` includes fileClient.py and server directory.

Directory `Server` includes fileServer.py

* fileClient.py : 
Establishes connection to server , then you input a name of a file if file exist it reads and sends the information to the server file 

* fileServer.py : 
waits for a connection, once established it resieves the read parts of the file and writes it into the server. 

* Use: 
Start fileServer.py first then fileClient.py next. After that follow propt as indecated in the client side.

fileClient.py|1711import os, socket, sys, tqdm

def Main():
    address = "127.0.0.1" # ip address
    port = 50000 # port number to connect to 
    bufferSize = 4096 #number of bytes to send each time
    clientSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create server socket

    print(f"[+] Conneting to {address}:{port}")
    clientSock.connect((address,port)) # connect to server socket
    print(f"[+] Connected.")

    while True:
        try:
            fileName = input("File Transfer Name:")
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
                f.close()
            # ask the client whether he wants to continue 
        ans = input('\nDo you want to continue(y/n) :') 
        if ans == 'y': 
            continue
        else: 
            break
    # close the connection
    clientSock.close()  

  
if __name__ == '__main__': 
    Main() 