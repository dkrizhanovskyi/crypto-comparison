import unittest
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from aes_example import encrypt, decrypt

class TestAESExample(unittest.TestCase):

    def test_encryption_decryption(self):
        key = get_random_bytes(16)  # AES-128
        message = b'This is a test message'
        
        nonce, ciphertext, tag = encrypt(message, key)
        plaintext = decrypt(nonce, ciphertext, tag, key)
        
        self.assertEqual(plaintext, message)

    def test_decryption_failure(self):
        key = get_random_bytes(16)  # AES-128
        wrong_key = get_random_bytes(16)
        message = b'This is a test message'
        
        nonce, ciphertext, tag = encrypt(message, key)
        plaintext = decrypt(nonce, ciphertext, tag, wrong_key)
        
        self.assertIsNone(plaintext)

if __name__ == '__main__':
    unittest.main()
