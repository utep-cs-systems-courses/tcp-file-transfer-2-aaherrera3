import socket, sys, re, os 
from framedSock import framedSend, framedReceive


def fileWrite(name, data, sock):
    name = "(Server)"+name
    if os.path.isfile(name):
        framedSend(sock, b"File already in server.", False)
        return
    try:
        with open(name, "wb") as f:
            f.write(data)
        f.close()
        framedSend(sock, b"File Transfered.", False)
    except Exception as e:
        print(f"[+] Error: {e}")
        



def Main():
    address = ""
    port = 50001

    serverSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSock.bind((address,port))
    serverSock.listen(5)

    flag = False

    while not flag:
        rc = os.fork()
        if not rc:
            try:
                conn, addr = serverSock.accept()
                fileName = framedReceive(conn, False)
                data = framedReceive(conn, False)

                if data:
                    fileName = fileName.decode()
                    data = data

                    fileWrite(fileName, data, conn)

            except Exception as e:
                print(f"[+] Error {e} ")
                flag = True
        
           
            


if __name__ == '__main__': 
    Main()                  