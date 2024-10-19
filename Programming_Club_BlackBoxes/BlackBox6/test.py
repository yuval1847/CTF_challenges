import base64
import hashlib

def decrypt(s:str):
    # The function gets a string
    # The function reutrn the string after decoding.
    return base64.b64decode(s).decode()

def encrypt(text:str):
    return base64.b64encode(text.encode()).decode()

# print(decrypt("UHJvZ3JhbW1lcnM=")) # Username
# print(decrypt("Q2hlY2tTdW09MHgxMA==")) # Checksum
# print(decrypt("cGFzcz02ZmRzMjM=")) # password

# print(encrypt("admin"))


# print(chr(ord("N")+(100-78)))

def HashToMD5(text:str):
    return hashlib.md5(text.encode()).hexdigest()
    
print(HashToMD5("helloworld!"))