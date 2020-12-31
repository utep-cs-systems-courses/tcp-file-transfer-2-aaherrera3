import socket, sys, re, os 
from framedSock import framedSend, framedReceive

def send(name, size, info):
    sock = serverConnect(info)
    buff = int(size)
    framedSend(sock, name.encode(), False)
    framedSend(sock, str(size).encode(), False)
                    
    with open(name, "rb") as f:
        payload = f.read(buff)
        framedSend(sock, payload.encode(), False)
    f.close()
    return framedReceive(sock, False)

def getFile():
    fileNames = input(f"[+] Input file name: ")
    if "exit" in fileNames:
        print("[+] Shuting down")
        sys.exit(1)
    try:
        fileSize = os.path.getsize(fileNames)
    except FileNotFoundError:
        print(f"[+] The file {fileNames} could not be found.")
    else:
        if fileSize == 0:
            print("[+] Empty File.")
        else:
            return fileNames , fileSize

def serverConnect(info):
    address = info[0]
    port = info[1]
    clientSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSock.connect((address, port))
    if clientSock is None:
        print("[+] Could not connect.")
        sys.exit(1)
    return clientSock

def Main():
    try:
        info = (sys.argv[1], int(sys.argv[2]))
    except IndexError:
        print("[+] Misssing argument -> python3 fileClient.py <addres> <prot>")
        sys.exit(1)


    while 1:

        name, size = getFile()

        respond = send(name, size, info)

        print(respond.decode())

        






if __name__ == '__main__': 
    Main()

