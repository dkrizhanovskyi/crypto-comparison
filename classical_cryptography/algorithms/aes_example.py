from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# Key generation
key = get_random_bytes(16)  # AES-128

# Encryption
def encrypt(message, key):
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(message)
    return nonce, ciphertext, tag

# Decryption
def decrypt(nonce, ciphertext, tag, key):
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt(ciphertext)
    try:
        cipher.verify(tag)
        return plaintext
    except ValueError:
        return None

# Example usage
message = b'This is a secret message'
nonce, ciphertext, tag = encrypt(message, key)
print(f'Ciphertext: {ciphertext}')

plaintext = decrypt(nonce, ciphertext, tag, key)
if plaintext:
    print(f'Plaintext: {plaintext.decode("utf-8")}')
else:
    print('Decryption failed')
