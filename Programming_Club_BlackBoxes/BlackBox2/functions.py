import base64

def decrypt(s:str):
    # The function gets a string.
    # The function returns the string after decrypting it.
    return base64.b64decode(s.encode()).decode()

def UTF8encrypt(s:str):
    # The function gets a string.
    # The function returns the string after encrypting it using utf-8.
    return base64.b64encode(s.encode()).decode()

print(decrypt("ODQxMjM0=="))
print("a43fa".encode().hex())