import base64

def decrypt(s:str):
    # The function gets a string.
    # The function returns the string after decrypting it.
    return base64.b64decode(s.encode()).decode()

def UTF8encrypt(s:str):
    # The function gets a string.
    # The function returns the string after encrypting it using utf-8.
    return base64.b64encode(s.encode()).decode()
    
def str_to_hex(s:str):
    # The function gets a string.
    # The function returns the hex representation of the given string.
    return s.encode().hex()

print(decrypt("ODQxMjM0=="))
print(str_to_hex("a43fa"))
print(str_to_hex("check_licence_registry"))