# tcp-ip


# TCP/IP Client-Server Programming

This repository contains various tasks related to **TCP/IP protocols**, focusing on client-server communication using both **TCP (stream)** and **UDP (datagram)** sockets.

---

## **Tasks**

### **1. TCP Synchronous Chat Program**
- Write a simple client-server program using a **stream (TCP)** socket that provides a synchronous chat facility.
- The application allows a user on one machine to type and send text to a user on another machine over the socket.

---

### **2. UDP Synchronous Chat Program**
- Repeat the above task using a **datagram (UDP)** socket.

---

### **3. Introduction to Sockets**

#### **a. Datagram Socket with Two Clients and One Server**
- Create three programs using a datagram socket, two of which are **clients** to a single **server**.
- **Client1** will send a character to the server.
- The **server** will decrement the letter to the next letter in the alphabet and send the result to **Client2**.
- **Client2** prints the letter it receives and then all the processes terminate.

---

#### **b. Send a C Structure**
- Send a C structure that includes data of type `character`, `integer`, and `float` from **Client1** to the **server**.
- The server modifies the values so that **Client2** receives a structure with entirely different data.
- **Note:** Data should **not** be converted to any other data type before transmission.

---

### **4. TCP Directory Service (Simple Client-Server)**
- Build a simple client-server application using Unix stream (TCP) sockets to implement a basic directory service.
- The server maintains a database (file) with address-name pairs, e.g.:
  ```
  0 Bob
  3 Anne
  5 Barb
  7 Ray
  9 Denbigh
  10 Terri
  104 John
  ```
- The client sends a numeric address to the server.
- The server looks up the address and sends back the matching name.
- If the address is not found, the server replies with an error message (e.g., "Address not found").

---

### **5. TCP Directory Service with Custom Protocol**
- Extend the previous directory service to use a custom protocol for message exchange.
- **Protocol Structure:**
  - **Requests:**
    - Byte 0: Request code (`0000001` for name lookup, `00001001` for number lookup)
    - Bytes 1-n: Request data (address or name)
    - Byte n+1: End-of-request (`00000011` (ETX))
  - **Replies:**
    - Bytes 0-n: Reply data (name or number, or error message)
    - Byte n+1: End-of-reply (`00000011` (ETX))
- The client can request by address or by name.
- The server responds with the corresponding name or address, or an error message if not found.
- The protocol supports binary data (e.g., sending a short integer as two bytes).

---

### **6. TCP Asynchronous Chat Program**
- Write a client-server program that provides an asynchronous chat facility using TCP sockets.
- The application allows a user on one machine to type and send text to a user on another machine at any time.
- The chat must be non-blocking: users can send any number of messages at any time without waiting for a reply from the other side.
- **Hint:** You may utilize the following system calls to implement non-blocking communication:
  - `select()`
  - `fork()`
  - `fcntl()`
- Choose the most suitable call as per your convenience and platform.

---

### **7. TCP File Transfer Program**
- Write a client-server program using stream (TCP) sockets to provide a file transfer facility.
- The client allows a user to request a file from the server.
- On request, the server transfers the file to the client.
- The client creates a file (e.g., `receive.txt`) and stores the data received from the server, then closes the file.
- **System calls to use:** `open()`, `creat()`, `read()`, `write()`
- **Usage:**
  ```
  $ ./a.out [server_address] [port_number] [file_name.txt]
  ```
  - `server_address`: IP address of the server
  - `port_number`: Port number of the server socket
  - `file_name.txt`: Name of the requested file
  - The received file is stored as `receive.txt` on the client side.

---

### **8. Concurrent TCP File Transfer Server**
- Implement a concurrent server for the above file transfer (FTP) application.
- The concurrent server can serve any number of clients simultaneously.
- **System call to use:** `fork()`
- Each client request is handled in a separate process, allowing multiple file transfers at the same time.

---

## **How to Run**
- For **C programs**, compile using:
  ```bash
  gcc filename.c -o output_name
  ./output_name


* For **Python programs**, run directly using:

  ```bash
  python filename.py
  ```
* **Always run the server first**, then start the client(s).
* Detailed steps will be added in each task's folder.

---

## **Repository Structure**

```
├── task1_tcp_chat/
│   ├──  client.py
│   └──  server.py
│
├── task2_udp_chat/
│   ├──  client.py
│   └──  server.py
│
├── task3_sockets/
│   ├── part_a/
│   │   ├── client1.c 
│   │   ├── client2.c 
│   │   └── server.c 
│   └── part_b/
│       ├── client1.c 
│       ├── client2.c 
│       └── server.c 
│
│
└── ...remaining
└── README.md
```

---


## **Requirements**

* C compiler (`gcc`) or Python (3.x)
* Linux/Unix environment (recommended)
* Basic knowledge of sockets

---


