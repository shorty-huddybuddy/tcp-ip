import socket

def chat_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 12345))

    while True:
        message = input("Client: ")
        client_socket.sendall(message.encode('utf-8'))

        if message.lower() == 'bye':
            break

        reply = client_socket.recv(1024).decode('utf-8')
        print("Server:", reply)

    client_socket.close()

if __name__ == "__main__":
    chat_client()

