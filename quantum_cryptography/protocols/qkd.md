# Quantum Key Distribution (QKD)

Quantum Key Distribution (QKD) is a method used to securely distribute cryptographic keys between two parties. The security of QKD is based on the principles of quantum mechanics, which makes it fundamentally different from classical key distribution methods.

## How QKD Works

### Preparation and Transmission

1. **Photon Generation**:
   - Alice prepares a sequence of photons, each in one of four possible polarization states: horizontal (0°), vertical (90°), +45°, and -45°.

2. **Transmission**:
   - Alice sends these photons to Bob through a quantum channel (e.g., optical fiber).

### Measurement

1. **Random Basis Selection**:
   - Bob randomly chooses a measurement basis (rectilinear or diagonal) for each incoming photon.

2. **Measurement**:
   - Bob measures the photons. Due to the Heisenberg Uncertainty Principle, each measurement disturbs the photon's state.

### Key Sifting

1. **Public Discussion**:
   - Alice and Bob publicly share which bases they used for each photon. They discard the results where their bases did not match.

2. **Key Extraction**:
   - The remaining results, where the bases matched, are used to form the raw key.

### Error Correction and Privacy Amplification

1. **Error Correction**:
   - Alice and Bob use classical communication to detect and correct any errors in the raw key.

2. **Privacy Amplification**:
   - They apply privacy amplification techniques to reduce any partial information that an eavesdropper (Eve) might have obtained, resulting in a shorter but more secure final key.

## Security

The security of QKD is guaranteed by the fundamental principles of quantum mechanics:

1. **Heisenberg Uncertainty Principle**: Any attempt to measure a quantum state without knowledge of the correct basis will disturb the state, revealing the presence of an eavesdropper.
2. **No-Cloning Theorem**: It is impossible to create an exact copy of an arbitrary unknown quantum state, preventing Eve from copying the key.

## Implementations

### BB84 Protocol

The BB84 protocol, proposed by Charles Bennett and Gilles Brassard in 1984, is the most well-known and widely used QKD protocol. It uses the polarization states of photons to encode the key.

### E91 Protocol

The E91 protocol, proposed by Artur Ekert in 1991, uses quantum entanglement to distribute the key. It is based on the principles of Bell's theorem.

## Applications

- **Secure Communications**: Used in high-security communication networks.
- **Government and Military**: Ensures the confidentiality of sensitive information.
- **Financial Services**: Protects financial transactions and sensitive data.

## References

- For more detailed information on QKD, see [Quantum Cryptography Wikipedia](https://en.wikipedia.org/wiki/Quantum_cryptography) and [IEEE Xplore](https://ieeexplore.ieee.org/).
