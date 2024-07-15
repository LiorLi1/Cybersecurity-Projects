import socket

SERVER_IP ="ENTER_IP_HERE"
PORT = ENTER_PORT_HERE
MAX_MSG_SIZE = 62
data="start"
checksum=""
msg=""
print("the main server is running at ip "+SERVER_IP+ "port :"+ str(PORT))
while(data != "exit"):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((SERVER_IP, PORT))
    (client_message, client_address) = server_socket.recvfrom(MAX_MSG_SIZE)
    data = client_message.decode()
    if "xor is :" in data:
        checksum=data
    else:
        msg=data
    response = data
    xor=0
    i=0
    while i < len(data):
        xor=xor^client_message[i]
        i+=1

    print("Server xor:"+str(xor))
    print(checksum)
    if xor is checksum:
        print("Client sent: "+msg)
    else:
        print("Corrupted packets, Dropping...")





server_socket.close()