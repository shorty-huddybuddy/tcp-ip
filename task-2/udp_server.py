import socket

def udp_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('127.0.0.1', 12345))

    print("UDP Server is listening...")

    while True:
        data, client_address = server_socket.recvfrom(1024)
        print("Received from", client_address, ":", data.decode('utf-8'))

        if data.decode('utf-8').lower() == 'bye':
            break

    print("Connection closed.")
    server_socket.close()

if __name__ == "__main__":
    udp_server()

