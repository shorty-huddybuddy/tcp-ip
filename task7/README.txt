Compile server.c  and client.c
	gcc server.c -o server
	gcc client.c -o client

Run the server first
	./server
The run the client file
	./client [server_address] [port_number] [file_name.txt]

The contents of file_name.txt will be copied to receive.txt.If receive.txt doesn't exist, it will be created. 
