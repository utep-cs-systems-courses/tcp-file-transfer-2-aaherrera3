import socket, sys, re, os 
from framedSock import framedSend, framedReceive

def Main():
    address = ""
    port = 50000
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket.bind((address,port))
    serverSocket.listen(5)



    while True:
        print(f"[+] Waiting For connection:")
        convSocket, clientAddress = serverSocket.accept()
        print(f"[+] Connected to {clientAddress}.")

        while convSocket:
            try:
                fileName = framedReceive(convSocket,False).decode()
                fileSize = framedReceive(convSocket,False).decode()

                fileName = os.path.basename(fileName)
                fileSize = int(fileSize)

                rc = os.fork()

                if rc < 0: # If fork fails 
                    os.write(2,("fork failed, returning %d\n" % rc).encode)
                    sys.exit(1)
                elif rc == 0:
                    with open("(Server)"+fileName, "wb") as f:
                        payload = framedReceive(convSocket, False)
                        if not payload:
                            print(f"[+] Transfer Complete.")
                        f.write(payload)
                    f.close()
            except AttributeError:
                print("[+] Connection Terminated")
        
            
        
        


if __name__ == "__main__":
    Main()