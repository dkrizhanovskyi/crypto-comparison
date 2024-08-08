from Crypto.PublicKey import ECC
from Crypto.Signature import DSS
from Crypto.Hash import SHA256

# Generate ECC keys
def generate_ecc_keys():
    private_key = ECC.generate(curve='P-256')
    public_key = private_key.public_key()
    return private_key, public_key

# Sign a message using ECC private key
def sign_message(message, private_key):
    h = SHA256.new(message)
    signer = DSS.new(private_key, 'fips-186-3')
    signature = signer.sign(h)
    return signature

# Verify a signature using ECC public key
def verify_signature(message, signature, public_key):
    h = SHA256.new(message)
    verifier = DSS.new(public_key, 'fips-186-3')
    try:
        verifier.verify(h, signature)
        return True
    except ValueError:
        return False

# Example usage
private_key, public_key = generate_ecc_keys()
message = b'This is a secret message'
signature = sign_message(message, private_key)
print(f'Signature: {signature}')

is_valid = verify_signature(message, signature, public_key)
print(f'Signature valid: {is_valid}')
