from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))

serverSocket.listen(1)
print('The server is ready to receive')

with open('directory.txt', 'r') as file:
    lines = file.readlines()
    dict = {}
    for line in lines:
        info = line.split()
        dict[info[0]] = info[1]


while True:
    connectionSocket, addr = serverSocket.accept()
    number = connectionSocket.recv(1024).decode()
    if number in dict:
        connectionSocket.send(dict[number].encode())
    else:
        msg = f"No user with the number {number}"
        connectionSocket.send(msg.encode())

    connectionSocket.close()
