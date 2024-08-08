import random

# Define basis and bits
def generate_basis_and_bits(length):
    basis = [random.choice(['+', 'x']) for _ in range(length)]
    bits = [random.randint(0, 1) for _ in range(length)]
    return basis, bits

# Encode bits to photons
def encode_bits(basis, bits):
    photons = []
    for b, bit in zip(basis, bits):
        if b == '+':
            photon = 'H' if bit == 0 else 'V'
        else:
            photon = 'D' if bit == 0 else 'A'
        photons.append(photon)
    return photons

# Measure photons
def measure_photons(received_photons, basis):
    measured_bits = []
    for photon, b in zip(received_photons, basis):
        if b == '+':
            bit = 0 if photon in ['H', 'D'] else 1
        else:
            bit = 0 if photon in ['D', 'H'] else 1
        measured_bits.append(bit)
    return measured_bits

# Key sifting
def sift_keys(sender_basis, receiver_basis, sender_bits, receiver_bits):
    sifted_key = []
    for sb, rb, sb_bit, rb_bit in zip(sender_basis, receiver_basis, sender_bits, receiver_bits):
        if sb == rb:
            sifted_key.append(sb_bit)
    return sifted_key

# Example usage
length = 100
alice_basis, alice_bits = generate_basis_and_bits(length)
alice_photons = encode_bits(alice_basis, alice_bits)

# Bob chooses his basis
bob_basis, _ = generate_basis_and_bits(length)
bob_bits = measure_photons(alice_photons, bob_basis)

# Key sifting
sifted_key = sift_keys(alice_basis, bob_basis, alice_bits, bob_bits)
print(f'Sifted Key: {sifted_key}')
