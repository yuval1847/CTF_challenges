# Ciphers:
import base64

def decrypt(s:str):
    # The function gets a string
    # The function returns the string converted
    return base64.b64decode(s).decode()

print(decrypt(""))

