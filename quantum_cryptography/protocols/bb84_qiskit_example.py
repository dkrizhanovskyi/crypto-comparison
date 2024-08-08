import random
from qiskit import QuantumCircuit, Aer, transpile, assemble, execute
from qiskit.visualization import plot_histogram

# BB84 protocol implementation

def generate_random_bits(length):
    return [random.randint(0, 1) for _ in range(length)]

def generate_random_bases(length):
    return [random.choice(['+', 'x']) for _ in range(length)]

def encode_bits_to_photons(bits, bases):
    photons = []
    for bit, base in zip(bits, bases):
        if base == '+':
            photon = '0' if bit == 0 else '1'
        else:
            photon = '+0' if bit == 0 else '+1'
        photons.append(photon)
    return photons

def measure_photons(photons, bases):
    measured_bits = []
    for photon, base in zip(photons, bases):
        if base == '+':
            bit = 0 if photon in ['0', '+0'] else 1
        else:
            bit = 0 if photon in ['+0', '0'] else 1
        measured_bits.append(bit)
    return measured_bits

def sift_keys(sender_bases, receiver_bases, sender_bits, receiver_bits):
    sifted_key = []
    for sb, rb, sb_bit, rb_bit in zip(sender_bases, receiver_bases, sender_bits, receiver_bits):
        if sb == rb:
            sifted_key.append(sb_bit)
    return sifted_key

# Example usage
length = 100
alice_bits = generate_random_bits(length)
alice_bases = generate_random_bases(length)
alice_photons = encode_bits_to_photons(alice_bits, alice_bases)

bob_bases = generate_random_bases(length)
bob_bits = measure_photons(alice_photons, bob_bases)

sifted_key = sift_keys(alice_bases, bob_bases, alice_bits, bob_bits)
print(f'Sifted Key: {sifted_key}')
