import unittest
from qkd_example import generate_basis_and_bits, encode_bits, measure_photons, sift_keys

class TestQKDExample(unittest.TestCase):

    def test_key_generation(self):
        length = 100
        alice_basis, alice_bits = generate_basis_and_bits(length)
        alice_photons = encode_bits(alice_basis, alice_bits)

        bob_basis, _ = generate_basis_and_bits(length)
        bob_bits = measure_photons(alice_photons, bob_basis)

        sifted_key = sift_keys(alice_basis, bob_basis, alice_bits, bob_bits)
        self.assertTrue(len(sifted_key) <= length)
        self.assertTrue(all(bit in [0, 1] for bit in sifted_key))

    def test_sifted_key_length(self):
        length = 100
        alice_basis, alice_bits = generate_basis_and_bits(length)
        alice_photons = encode_bits(alice_basis, alice_bits)

        bob_basis, _ = generate_basis_and_bits(length)
        bob_bits = measure_photons(alice_photons, bob_basis)

        sifted_key = sift_keys(alice_basis, bob_basis, alice_bits, bob_bits)
        matching_basis_count = sum(1 for a, b in zip(alice_basis, bob_basis) if a == b)
        self.assertEqual(len(sifted_key), matching_basis_count)

if __name__ == '__main__':
    unittest.main()
