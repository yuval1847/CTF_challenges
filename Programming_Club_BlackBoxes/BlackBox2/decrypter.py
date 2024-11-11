import base64

def decrypt(s:str):
    # The function gets a string.
    # The function returns the string after decrypting it.
    return base64.b64decode(s.encode()).decode()

print(decrypt("ODQxMjM0=="))