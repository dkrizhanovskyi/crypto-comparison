from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Random import get_random_bytes

# Key generation
key = RSA.generate(2048)
private_key = key.export_key()
public_key = key.publickey().export_key()

# Save keys to files
with open('private.pem', 'wb') as f:
    f.write(private_key)

with open('public.pem', 'wb') as f:
    f.write(public_key)

# Encryption
message = b'This is a secret message'
cipher_rsa = PKCS1_OAEP.new(key.publickey())
ciphertext = cipher_rsa.encrypt(message)

# Decryption
cipher_rsa = PKCS1_OAEP.new(key)
plaintext = cipher_rsa.decrypt(ciphertext)
print(plaintext.decode('utf-8'))
