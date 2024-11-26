# Sockets stuff
import socket

# A UDP socket
# s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# s.bind(('127.0.0.1', 12345))

# while True:
#     print("****************************************")
#     print(s.recvfrom(4096)[0].decode())


# A TCP socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 8543))
s.send("1234".encode())
while True:
    print("****************************************")
    print(s.recv(4096).decode())