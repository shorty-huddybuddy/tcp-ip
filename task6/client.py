import socket
import sys
import select

client=socket.socket()
host=socket.gethostbyname(socket.gethostname())
port=1234
addr=(host,port)
client.connect(addr)

iobuffer=[client,sys.stdin]

flag=True

print("wellcome to client side")
print("q for exit")

while True:
    rl,wl,el=select.select(iobuffer,[],[])
    for r in rl:
        if r is client:
            msg=client.recv(2048).decode()
            print("server:",msg)
            if msg=='q':
                client.send("thank you".encode())
                flag=False
                break
        else :
            msg=input()
            client.send(msg.encode())
            if msg=='q':
                flag=False
                break

    if not (flag):
        break

print("thank you")
client.close()
