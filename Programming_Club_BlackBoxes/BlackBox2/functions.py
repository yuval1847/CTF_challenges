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

def generate_sha1_hash(input_string:str):
    # The function gets a string.
    # The function returns the hash of the given string according to SHA-1.
    sha1_hash = hashlib.sha1()
    sha1_hash.update(input_string.encode())
    return sha1_hash.hexdigest()

def generate_phonenumber_bruteforce():
    # Bruteforcing
    for a in range(10):
        for b in range(10):
            for c in range(10):
                for d in range(10):
                    for e in range(10):
                        for f in range(10):
                            for g in range(10):
                                for h in range(10):
                                    for i in range(10):
                                        for j in range(10):
                                            print(f"{a}{b}{c}{d}{e}{f}{g}{h}{i}{j}")
                                            yield f"{a}{b}{c}{d}{e}{f}{g}{h}{i}{j}"

def t():
    print("Brutefoce Started!")
    for phone_number in generate_phonenumber_bruteforce():
        if generate_sha1_hash(phone_number) == "6688795677c1c8f2d3cd14b710f60153":
            print(f"The phone nubmer of the hash is: {phone_number}")

if __name__ == "__main__":
    th = threading.Thread(target=t)
    th.start()