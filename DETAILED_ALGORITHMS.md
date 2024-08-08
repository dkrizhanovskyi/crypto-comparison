# Detailed Descriptions of Cryptographic Algorithms

This document provides detailed descriptions of various cryptographic algorithms used in classical and quantum cryptography. Each algorithm is explained with its principles, security aspects, and example implementations.

## Classical Cryptographic Algorithms

### RSA (Rivest-Shamir-Adleman)

RSA is an asymmetric cryptographic algorithm based on the mathematical difficulty of factoring large integers.

- **Principles**: Uses a pair of keys, public and private, for encryption and decryption. Security relies on the difficulty of factoring the product of two large prime numbers.
- **Security**: Secure with key sizes of 2048 bits or more. Vulnerable to quantum attacks.
- **Example Implementation**: See `classical_cryptography/algorithms/rsa_example.py`.

### AES (Advanced Encryption Standard)

AES is a symmetric encryption algorithm widely used for securing data.

- **Principles**: Uses the same key for both encryption and decryption. Operates on fixed block sizes of 128 bits with key sizes of 128, 192, or 256 bits.
- **Security**: Considered secure when using sufficient key lengths (128 bits or more). Resistant to known cryptographic attacks.
- **Example Implementation**: See `classical_cryptography/algorithms/aes_example.py`.

### ECC (Elliptic Curve Cryptography)

ECC is an asymmetric cryptographic algorithm based on the algebraic structure of elliptic curves over finite fields.

- **Principles**: Uses elliptic curves to generate public and private keys. Provides strong security with smaller key sizes compared to RSA.
- **Security**: Secure against classical attacks and provides strong security with smaller key sizes (e.g., 256-bit ECC key is comparable to a 3072-bit RSA key). Vulnerable to quantum attacks.
- **Example Implementation**: See `classical_cryptography/algorithms/ecc_example.py`.

## Quantum Cryptographic Protocols

### Quantum Key Distribution (QKD)

QKD uses principles of quantum mechanics to securely distribute cryptographic keys.

- **Principles**: Relies on quantum states and the Heisenberg Uncertainty Principle to detect eavesdropping. The most common protocol is BB84.
- **Security**: Provides unconditional security based on the laws of quantum mechanics. Immune to quantum attacks.
- **Example Implementation**: See `quantum_cryptography/protocols/qkd_example.py`.

### BB84 Protocol

BB84 is a QKD protocol that uses photon polarization states to encode and distribute keys.

- **Principles**: Uses random bases for encoding and measuring photon states. Key sifting is performed to generate a secure shared key.
- **Security**: Provides security against eavesdropping based on quantum mechanics.
- **Example Implementation**: See `quantum_cryptography/protocols/bb84_example.py`.

### Grover's Algorithm

Grover's algorithm is a quantum algorithm that provides a quadratic speedup for unstructured search problems.

- **Principles**: Uses quantum superposition and interference to search an unsorted database in \(O(\sqrt{N})\) time.
- **Security**: Demonstrates the power of quantum computing in solving specific problems faster than classical algorithms.
- **Example Implementation**: See `quantum_cryptography/protocols/grover_example.py`.

### Quantum Teleportation

Quantum teleportation is a protocol for transferring quantum states between distant locations using entanglement.

- **Principles**: Uses entangled particles and classical communication to transfer quantum information.
- **Security**: Demonstrates fundamental quantum principles and can be used in quantum communication.
- **Example Implementation**: See `quantum_cryptography/protocols/quantum_teleportation_example.py`.

## References

- For more detailed information on cryptographic algorithms, see resources such as [SpringerLink](https://link.springer.com/), [arXiv](https://arxiv.org/), and [IEEE Xplore](https://ieeexplore.ieee.org/).
- Additional details on quantum cryptography can be found on [Quantum Cryptography Wikipedia](https://en.wikipedia.org/wiki/Quantum_cryptography).
