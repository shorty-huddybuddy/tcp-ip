import socket

def chat_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 12345))
    server_socket.listen(1)

    print("Server is listening for incoming connections...")

    client_socket, client_address = server_socket.accept()
    print("Connected to:", client_address)

    while True:
        message = client_socket.recv(1024).decode('utf-8')
        print("Client:", message)

        if message.lower() == 'bye':
            break

        reply = input("Server: ")
        client_socket.sendall(reply.encode('utf-8'))

    print("Connection closed.")
    server_socket.close()

if __name__ == "__main__":
    chat_server()

