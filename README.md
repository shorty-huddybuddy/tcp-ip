# tcp-ip

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
- Compile each program using `gcc` (or your preferred compiler).
- Run the server first, then the client(s).
- Detailed steps will be added in each task's folder.

---

## **Repository Structure**
