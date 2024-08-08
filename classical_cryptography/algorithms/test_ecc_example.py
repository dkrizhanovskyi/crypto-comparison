import unittest
from Crypto.PublicKey import ECC
from ecc_example import sign_message, verify_signature

class TestECCExample(unittest.TestCase):

    def setUp(self):
        self.private_key = ECC.generate(curve='P-256')
        self.public_key = self.private_key.public_key()

    def test_signature_verification(self):
        message = b'This is a test message'
        signature = sign_message(message, self.private_key)
        is_valid = verify_signature(message, signature, self.public_key)
        self.assertTrue(is_valid)

    def test_signature_failure(self):
        message = b'This is a test message'
        wrong_message = b'This is a different message'
        signature = sign_message(message, self.private_key)
        is_valid = verify_signature(wrong_message, signature, self.public_key)
        self.assertFalse(is_valid)

if __name__ == '__main__':
    unittest.main()
