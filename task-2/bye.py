import socket

def udp_client3():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    message = "bye"
    client_socket.sendto(message.encode('utf-8'), ('127.0.0.1', 12345))
    client_socket.close()

if __name__ == "__main__":
    udp_client3()

