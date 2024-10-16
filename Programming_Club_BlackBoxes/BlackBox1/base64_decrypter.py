import base64

def decrypt(encrypted_text:str):
    # The function gets a string.
    # The function returns the given string after decrypting it.
    return base64.b64decode(encrypted_text).decode()

def encrypt(text:str):
    # The function gets a string.
    # The function returns the given string after encrypting it.
    return base64.b64encode(text.encode()).decode()

print(encrypt("admin123"))