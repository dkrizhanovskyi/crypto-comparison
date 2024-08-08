from Crypto.PublicKey import ECC
from Crypto.Signature import DSS
from Crypto.Hash import SHA256

# Key generation
private_key = ECC.generate(curve='P-256')
public_key = private_key.public_key()

# Save keys to files
with open('ecc_private.pem', 'wt') as f:
    f.write(private_key.export_key(format='PEM'))

with open('ecc_public.pem', 'wt') as f:
    f.write(public_key.export_key(format='PEM'))

# Sign a message
def sign_message(message, private_key):
    h = SHA256.new(message)
    signer = DSS.new(private_key, 'fips-186-3')
    signature = signer.sign(h)
    return signature

# Verify a signature
def verify_signature(message, signature, public_key):
    h = SHA256.new(message)
    verifier = DSS.new(public_key, 'fips-186-3')
    try:
        verifier.verify(h, signature)
        return True
    except ValueError:
        return False

# Example usage
message = b'This is a message to be signed'
signature = sign_message(message, private_key)
print(f'Signature: {signature}')

is_valid = verify_signature(message, signature, public_key)
print(f'Signature valid: {is_valid}')
