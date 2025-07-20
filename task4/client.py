from socket import *
servername = 'localhost'
serverport = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((servername, serverport))

raw_sentence = input()

clientSocket.send(raw_sentence.encode())

name = clientSocket.recv(1024)

print(name.decode())

clientSocket.close()
