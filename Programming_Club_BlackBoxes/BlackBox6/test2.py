import socket

HOST = "127.0.0.1"
PORT = 8085

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
data = s.recv(1024)
print(data)