import socket, sys, re, os 
from framedSock import framedSend, framedReceive


def Main():
    address = sys.argv[1]
    port =  int(sys.argv[2])
    bufferSize = 4096
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    print(f"[+] Connecting to {address}:{port}")
    clientSocket.connect((address, port))
    print(f"[+] Connected.")

    flag = 1

    while flag:
        fileNames = input(f"[+] Input file name: ")
        fileNames = fileNames.split(' ')

        for name in fileNames:
            try:
                fileSize = os.path.getsize(name)
                print(f"File Size: {fileSize}")
            except FileNotFoundError:
                print(f"[+] The file {name} could not be found.")
            else:
                if fileSize == 0:
                    print("[+] Empty File.")
                else:
                    framedSend(clientSocket, name.encode(), False)
                    framedSend(clientSocket, str(fileSize).encode(), False)
                    
                    with open(name, "rb") as f:
                        payload = f.read(bufferSize)
                        framedSend(clientSocket, payload, False)
                    f.close()
        flag = int(input("[+] continue (1 for yes, 0 for no)? "))
     
    print(f"[+] Terminating Connection:")
    clientSocket.close()
    print(f"[+] Terminated")

if __name__ == "__main__":
    Main()