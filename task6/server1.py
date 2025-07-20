import socket
import sys
import select
import threading

def client_handler(c):
    iobuffer = [c, sys.stdin]
    while True:
        rs, ws, es = select.select(iobuffer, [], [])
        for r in rs:
            if r is c:
                msg = c.recv(2084).decode()
                print("client:", msg)
                if msg == 'q':
                    print("terminated")
                    c.close()
                    return
            else:
                msg = input()
                if msg == 'q':
                    c.send(msg.encode())
                    c.close()
                    return
                else:
                    c.send(msg.encode())

s = socket.socket()
host = socket.gethostbyname(socket.gethostname())
port = 1234

addr = (host, port)
s.bind(addr)
s.listen(5)  # Number of connections to be queued
print("Server listening on", addr)

while True:
    c, adr = s.accept()
    print('Connected to', adr)
    # Start a new thread to handle the client
    threading.Thread(target=client_handler, args=(c,)).start()

s.close()
