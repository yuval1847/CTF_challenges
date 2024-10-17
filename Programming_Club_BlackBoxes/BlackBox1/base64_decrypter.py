import base64
import hashlib

def decrypt(encrypted_text:str):
    # The function gets a string.
    # The function returns the given string after decrypting it.
    return base64.b64decode(encrypted_text).decode()


def encrypt(text:str):
    # The function gets a string.
    # The function returns the given string after encrypting it.
    return base64.b64encode(text.encode()).decode()



def generate_sha1_hash(input_string:str):
    # The function gets a string.
    # The function returns the hash of the given string according to SHA-1.
    sha1_hash = hashlib.sha1()
    sha1_hash.update(input_string.encode())
    return sha1_hash.hexdigest()

if __name__ == "__main__":
    print(generate_sha1_hash("17/10/2024"))