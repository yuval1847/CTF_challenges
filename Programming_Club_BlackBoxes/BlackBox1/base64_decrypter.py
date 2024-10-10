import base64

def decrypt(encrypted_text):
    # The function gets a string.
    # The function returns the given string after decrypting it.
    return base64.b64decode(encrypted_text).decode()

print(decrypt("MTIzNA=="))