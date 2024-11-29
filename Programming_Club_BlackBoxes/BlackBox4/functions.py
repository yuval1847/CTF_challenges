import base64

def decrypt(s:str):
    # The function gets a string.
    # The function returns the given string after getting decrypted.
    return base64.b64decode(s.encode()).decode()

if __name__ == "__main__":
    print(decrypt("aHR0cDovLzEyNy4wLjAuMTo1MDAwL2ZpbmFsLXN0ZXA="))