import unittest
from bb84_example import generate_random_bits_and_basis, encode_bits_to_photons, measure_photons, sift_keys

class TestBB84Example(unittest.TestCase):

    def test_key_generation(self):
        length = 100
        alice_bits, alice_basis = generate_random_bits_and_basis(length)
        alice_photons = encode_bits_to_photons(alice_bits, alice_basis)

        bob_basis, _ = generate_random_bits_and_basis(length)
        bob_bits = measure_photons(alice_photons, bob_basis)

        sifted_key = sift_keys(alice_basis, bob_basis, alice_bits, bob_bits)
        self.assertTrue(len(sifted_key) <= length)
        self.assertTrue(all(bit in [0, 1] for bit in sifted_key))

    def test_sifted_key_length(self):
        length = 100
        alice_bits, alice_basis = generate_random_bits_and_basis(length)
        alice_photons = encode_bits_to_photons(alice_bits, alice_basis)

        bob_basis, _ = generate_random_bits_and_basis(length)
        bob_bits = measure_photons(alice_photons, bob_basis)

        sifted_key = sift_keys(alice_basis, bob_basis, alice_bits, bob_bits)
        matching_basis_count = sum(1 for a, b in zip(alice_basis, bob_basis) if a == b)
        self.assertEqual(len(sifted_key), matching_basis_count)

