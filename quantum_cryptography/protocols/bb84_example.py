import random

# Generate random bits and basis
def generate_random_bits_and_basis(length):
    bits = [random.randint(0, 1) for _ in range(length)]
    basis = [random.choice(['+', 'x']) for _ in range(length)]
    return bits, basis

# Encode bits into photons based on basis
def encode_bits_to_photons(bits, basis):
    photons = []
    for bit, b in zip(bits, basis):
        if b == '+':
            photon = 'H' if bit == 0 else 'V'
        else:
            photon = 'D' if bit == 0 else 'A'
        photons.append(photon)
    return photons

# Measure photons using basis
def measure_photons(photons, basis):
    measured_bits = []
    for photon, b in zip(photons, basis):
        if b == '+':
            bit = 0 if photon == 'H' else 1
        else:
            bit = 0 if photon == 'D' else 1
        measured_bits.append(bit)
    return measured_bits

# Sift keys based on matching basis
def sift_keys(sender_basis, receiver_basis, sender_bits, receiver_bits):
    sifted_key = []
    for sb, rb, sbit, rbit in zip(sender_basis, receiver_basis, sender_bits, receiver_bits):
        if sb == rb:
            sifted_key.append(sbit)
    return sifted_key

# Example usage
length = 100
alice_bits, alice_basis = generate_random_bits_and_basis(length)
alice_photons = encode_bits_to_photons(alice_bits, alice_basis)

bob_basis, _ = generate_random_bits_and_basis(length)
bob_bits = measure_photons(alice_photons, bob_basis)

sifted_key = sift_keys(alice_basis, bob_basis, alice_bits, bob_bits)
print(f'Sifted Key: {sifted_key}')
