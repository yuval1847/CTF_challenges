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



def generate_sha1_hash(input_string):
    # Encode the input string to bytes
    input_bytes = input_string.encode('utf-8')
    
    # Create a new SHA-1 hash object
    sha1_hash = hashlib.sha1()
    
    # Update the hash object with the bytes of the input string
    sha1_hash.update(input_bytes)
    
    # Get the hexadecimal representation of the hash
    hashed_string = sha1_hash.hexdigest()
    
    return hashed_string


print(generate_sha1_hash("""{"action": "login", "username": "admin", "token": "Y3liZXI="}"""))