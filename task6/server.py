import socket
import sys
import select


s=socket.socket()
host=socket.gethostbyname(socket.gethostname())
port=1234

addr=(host,port)
s.bind(addr)
s.listen(2)

c,adr=s.accept()

iobuffer =[c,sys.stdin]
# print("wellcome")
# print("q for exit")
flag=True
while True:
    rs,ws,es=select.select(iobuffer,[],[])
    for r in rs:
        if r is c:
            msg=c.recv(2084).decode()
            print("client:",msg)
            if msg=='q':
                print("terminated")
                c.close()
                flag=False
                break
        else :
            msg=input()
            if msg=='q':
                c.send(msg.encode())
                flag=False
                break
            else :
                c.send(msg.encode())
    if not (flag):
        break

s.close()
