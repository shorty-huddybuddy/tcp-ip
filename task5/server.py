import socket

# Database mapping numeric addresses to names
database = {
    '0': 'Bob',
    '3': 'Anne',
    '5': 'Barb',
    '7': 'Ray',
    '9': 'Denbigh',
    '10': 'Terri',
    '104': 'John'
}


def handle_request(request_data):
    request_code = request_data[:8]  # Extract the request code

    if request_code == "00000001":  # Request for a name
        name = request_data[8:-8].lower()  # Extract name

        # print(name)
        for num_address, db_name in database.items():
            if db_name.lower() == name:
                return num_address
        else:
            return "Address not found"

    elif request_code == "00001001":  # Request for a number
        numeric_address = request_data[8:-8]  # Extract numeric address
        if numeric_address in database:
            return database[numeric_address]
        else:
            return "Name not found"


def server():
    host = '127.0.0.1'
    port = 12345

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen(1)
        print("Server listening on {}:{}".format(host, port))

        while True:
            conn, addr = s.accept()
            with conn:
                print('Connected by', addr)
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break

                    # Decode received data
                    request_data = data.decode()

                    # Process request
                    response_data = handle_request(request_data)

                    # Encode response data
                    response = response_data.encode()

                    # Send response
                    conn.sendall(response)


if __name__ == "__main__":
    server()
