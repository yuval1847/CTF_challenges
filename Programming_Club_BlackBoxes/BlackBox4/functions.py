# import base64

# def decrypt(s:str):
#     # The function gets a string.
#     # The function returns the given string after getting decrypted.
#     return base64.b64decode(s.encode()).decode()

# if __name__ == "__main__":
#     print(decrypt("aHR0cDovLzEyNy4wLjAuMTo1MDAwL2ZpbmFsLXN0ZXA="))

import socket

HOST, PORT = "127.0.0.1", 8753

# A tcp socket:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))