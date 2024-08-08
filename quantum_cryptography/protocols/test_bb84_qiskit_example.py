import unittest
from bb84_qiskit_example import generate_random_bits, generate_random_bases, encode_bits_to_photons, measure_photons, sift_keys

class TestBB84QiskitExample(unittest.TestCase):

    def test_key_generation(self):
        length = 100
        alice_bits = generate_random_bits(length)
        alice_bases = generate_random_bases(length)
        alice_photons = encode_bits_to_photons(alice_bits, alice_bases)

        bob_bases = generate_random_bases(length)
        bob_bits = measure_photons(alice_photons, bob_bases)

        sifted_key = sift_keys(alice_bases, bob_bases, alice_bits, bob_bits)
        self.assertTrue(len(sifted_key) <= length)
        self.assertTrue(all(bit in [0, 1] for bit in sifted_key))

    def test_sifted_key_length(self):
        length = 100
        alice_bits = generate_random_bits(length)
        alice_bases = generate_random_bases(length)
        alice_photons = encode_bits_to_photons(alice_bits, alice_bases)

        bob_bases = generate_random_bases(length)
        bob_bits = measure_photons(alice_photons, bob_bases)

        sifted_key = sift_keys(alice_bases, bob_bases, alice_bits, bob_bits)
        matching_basis_count = sum(1 for a, b in zip(alice_bases, bob_bases) if a == b)
        self.assertEqual(len(sifted_key), matching_basis_count)

if __name__ == '__main__':
    unittest.main()
