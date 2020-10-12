import os, socket, threading, tqdm
from _thread import *

printLock = threading.Lock() #Protect values againsst simultaneous access from mult threads

def threaded(c):
    bufferSize = 4096 #number of bytes to send each time
    while True: 
        fileInfo = c.recv(bufferSize).decode() # get file info 
        fileName, fileSize = fileInfo.split("|") # split file info 

        fileName = os.path.basename(fileName) # remove absolute path
        fileSize = int(fileSize) # conver to int
        progress = tqdm.tqdm(range(fileSize), f"Sending {fileName}", unit="B", unit_scale=True, unit_divisor=1024)
        
        with open("(Server)"+fileName, "wb") as f:
            for _ in progress:
                bytesRead = c.recv(bufferSize) # recevive 4096 bytes from client
                if not bytesRead:
                    print("File Transfer Complete")
                    break #file transfer done
                f.write(bytesRead) # Write 4096 to server file
                progress.update(len(bytesRead)) # update progress bar
        c.close()

def Main():
    address = "" #default ip for server 
    port = 50000 # port number hosting
    serverSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create server socket
    serverSock.bind((address,port)) # bind socket to port 50001 and let it chose the address 
    serverSock.listen(5) # have the server socket in listen mode to 5 connection 
    while True:
        print(f"[+]Waiting for connection.")
        convSock, clienAddress = serverSock.accept() #creation of connection scoket
        printLock.acquire()
        print(f"[+] Connection to {clienAddress}.")

        start_new_thread(threaded, (convSock,))
    serverSock.close()

if __name__ == "__main__":
    Main()