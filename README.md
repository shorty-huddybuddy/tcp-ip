# tcp-ip

Here’s the **final `README.md`** file for your repository:


# TCP/IP Client-Server Tasks

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
│   ├── client.c / client.py
│   └── server.c / server.py
│
├── task2_udp_chat/
│   ├── client.c / client.py
│   └── server.c / server.py
│
├── task3_sockets/
│   ├── part_a/
│   │   ├── client1.c / client1.py
│   │   ├── client2.c / client2.py
│   │   └── server.c / server.py
│   └── part_b/
│       ├── client1.c / client1.py
│       ├── client2.c / client2.py
│       └── server.c / server.py
└── README.md
```

---

## **Requirements**

* C compiler (`gcc`) or Python (3.x)
* Linux/Unix environment (recommended)
* Basic knowledge of sockets

---



