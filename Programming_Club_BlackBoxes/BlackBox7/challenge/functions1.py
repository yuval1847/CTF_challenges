import base64

def decrypt(s:str):
    return base64.b64decode(s.encode()).decode()

def encrypt(s:str):
    return base64.b64encode(s.encode()).decode()

print(encrypt("help"))
