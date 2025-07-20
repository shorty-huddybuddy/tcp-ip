import socket


def client():
    host = '127.0.0.1'
    port = 12345

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))

        while True:
            # Prompt the user to input a request type
            request_type = input(
                "Enter request type (name/number), or 'q' to quit: ").lower()
            if request_type == 'q':
                break

            # Prompt the user to input a value
            value = input("Enter value: ")

            # Construct request according to protocol
            if request_type == 'name':
                request_data = "00000001" + value + "00000011"  # Request for a name
            elif request_type == 'number':
                request_data = "00001001" + value + "00000011"  # Request for a number
            else:
                print("Invalid request type. Please enter 'name' or 'number'.")
                continue

            # Send request
            s.sendall(request_data.encode())

            # Receive and decode response
            response_data = s.recv(1024).decode()

            # Print response
            print("Received:", response_data)


if __name__ == "__main__":
    client()
