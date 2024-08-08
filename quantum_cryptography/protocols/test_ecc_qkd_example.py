import unittest
from ecc_qkd_example import generate_ecc_keys, sign_message, verify_signature

class TestECCQKDExample(unittest.TestCase):

    def setUp(self):
        self.private_key, self.public_key = generate_ecc_keys()

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
