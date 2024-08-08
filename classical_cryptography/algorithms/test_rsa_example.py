import unittest
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

class TestRSAExample(unittest.TestCase):

    def test_encryption_decryption(self):
        # Key generation
        key = RSA.generate(2048)
        public_key = key.publickey()

        # Encryption
        message = b'This is a test message'
        cipher_rsa = PKCS1_OAEP.new(public_key)
        ciphertext = cipher_rsa.encrypt(message)

        # Decryption
        cipher_rsa = PKCS1_OAEP.new(key)
        plaintext = cipher_rsa.decrypt(ciphertext)
        
        self.assertEqual(plaintext, message)

if __name__ == '__main__':
    unittest.main()
