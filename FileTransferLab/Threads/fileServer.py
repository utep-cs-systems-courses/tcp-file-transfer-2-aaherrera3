import socket, sys, re, os 
from framedSock import framedSend, framedReceive
from threading import Thread, Lock
import time

class Server(Thread):
    def __init__(self,sock):
        self.sock = sock
        Thread.__init__(self)
        self.lock = Lock()

    def run(self):
        time.sleep(30)
        self.lock.acquire()
        try:
            fileName = framedReceive(self.sock,False)
            data = framedReceive(self.sock,False)

            if data:
                fileName =os.path.basename(fileName.decode())
                fileWrite(fileName,data,self.sock)
                self.lock.release()
                return True
        except Exception as e:
            print(f"[+] Error: {e}")
            return False
       
           


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
        conn, addr = serverSock.accept()
        server = Server(conn)
        flag = server.start()
        
        
if __name__ == '__main__': 
    Main()                  
