import socket

PORT = 5555
IP = "127.0.0.1"

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.connect((IP, PORT))

msg = input("Enter your message\n")
my_socket.send(msg.encode())
data = my_socket.recv(1024).decode()
print("The server sent " + data)


msg = input("Enter your message\n")
while msg != "":
    my_socket.send(msg.encode())
    data = my_socket.recv(1024).decode()
    print("The server sent " + data)
    msg = input("Enter your message\n")

my_socket.close()

