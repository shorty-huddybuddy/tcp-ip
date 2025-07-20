#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <sys/socket.h>

#define BUFFER_SIZE 1024

int main(int argc, char *argv[]) {
    if (argc != 4) {
        printf("Usage: %s [server_address] [port_number] [file_name.txt]\n", argv[0]);
        exit(EXIT_FAILURE);
    }

    // Create socket
    int client_socket = socket(AF_INET, SOCK_STREAM, 0);
    if (client_socket == -1) {
        perror("Socket creation failed");
        exit(EXIT_FAILURE);
    }

    // Connect to server
    struct sockaddr_in server_addr;
    server_addr.sin_family = AF_INET;
    server_addr.sin_port = htons(atoi(argv[2]));

    if (inet_pton(AF_INET, argv[1], &server_addr.sin_addr) <= 0) {
        perror("Invalid address/ Address not supported");
        exit(EXIT_FAILURE);
    }

    if (connect(client_socket, (struct sockaddr *)&server_addr, sizeof(server_addr)) == -1) {
        perror("Connection failed");
        exit(EXIT_FAILURE);
    }

    // Send file name to server
    if (send(client_socket, argv[3], strlen(argv[3]), 0) == -1) {
        perror("Send failed");
        exit(EXIT_FAILURE);
    }

    // Receive file contents from server
    FILE *file = fopen("receive.txt", "w");
    if (file == NULL) {
        perror("File creation failed");
        exit(EXIT_FAILURE);
    }

    char buffer[BUFFER_SIZE];
    long bytes_received;
    while ((bytes_received = recv(client_socket, buffer, sizeof(buffer), 0)) > 0) {
        fwrite(buffer, 1, bytes_received, file);
    }
    if (bytes_received == -1) {
        perror("Receive failed");
        exit(EXIT_FAILURE);
    }

    printf("File received successfully\n");

    // Close socket and file
    fclose(file);
    close(client_socket);

    return 0;
}
