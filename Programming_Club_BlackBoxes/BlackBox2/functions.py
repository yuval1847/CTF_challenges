import base64
import hashlib
import threading

def decrypt(s:str):
    # The function gets a string.
    # The function returns the string after decrypting it.
    return base64.b64decode(s.encode()).decode()

def UTF8encrypt(s:str):
    # The function gets a string.
    # The function returns the string after encrypting it using utf-8.
    return base64.b64encode(s.encode()).decode()
    
def str_to_hex(s:str):
    # The function gets a string which representing a decimal value.
    # The function returns the hex representation of the given string.
    return s.encode().hex()

#*****************************************************************************

def generate_sha1_hash(input_string:str):
    # The function gets a string.
    # The function returns the hash of the given string according to SHA-1.
    sha1_hash = hashlib.sha1()
    sha1_hash.update(input_string.encode())
    return sha1_hash.hexdigest()
    
def generate_md5_hash(input_string:str):
    # The function gets a string.
    # The function returns the hash of the given string according to SHA-1.
    sha1_hash = hashlib.md5()
    sha1_hash.update(input_string.encode())
    return sha1_hash.hexdigest()

def generate_phonenumber_bruteforce():
    # Bruteforcing
    for a in range(10):
        for b in range(10):
            for c in range(10):
                for d in range(10):
                    print(f"{a}{b}{c}{d}")
                    yield "052538" + f"{a}{b}{c}{d}"

# print("Bruteforce Started!")
# for phone_number in generate_phonenumber_bruteforce():
#     if generate_sha1_hash(phone_number) == "6688795677c1c8f2d3cd14b710f60153":
#         print(f"The phone number of the hash is: {phone_number}. The correct hash is: sha-1")
#         break
#     elif generate_md5_hash(phone_number) == "6688795677c1c8f2d3cd14b710f60153":
#         print(f"The phone number of the hash is: {phone_number}. The correct hash is: md5")
#         break

print(decrypt("bWdkZjMyZ2Y0M0AAAAAAAA==").encode())