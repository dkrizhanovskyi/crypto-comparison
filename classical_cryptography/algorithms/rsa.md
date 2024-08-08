# RSA

RSA (Rivest-Shamir-Adleman) is an asymmetric cryptographic algorithm that relies on the mathematical difficulty of factoring large integers. It uses a pair of keys — a public key for encryption and a private key for decryption.

## How RSA Works

1. **Key Generation**:
   - Choose two large prime numbers, \( p \) and \( q \).
   - Compute \( n = p \times q \).
   - Compute the totient \( \phi(n) = (p-1) \times (q-1) \).
   - Choose an integer \( e \) such that \( 1 < e < \phi(n) \) and \( \text{gcd}(e, \phi(n)) = 1 \).
   - Compute \( d \) such that \( d \times e \equiv 1 \ (\text{mod} \ \phi(n)) \).

   The public key is \( (n, e) \) and the private key is \( (n, d) \).

2. **Encryption**:
   - Convert the plaintext message \( M \) to an integer \( m \) such that \( 0 \leq m < n \).
   - Compute the ciphertext \( c \) using the public key: \( c = m^e \ (\text{mod} \ n) \).

3. **Decryption**:
   - Compute the original message \( m \) using the private key: \( m = c^d \ (\text{mod} \ n) \).
   - Convert \( m \) back to the plaintext message \( M \).

## Security

The security of RSA relies on the computational difficulty of factoring the large integer \( n \). As long as \( n \) is sufficiently large (typically 2048 bits or more), RSA is considered secure against current computational capabilities.

## Applications

- **Secure Communications**: RSA is widely used for secure data transmission.
- **Digital Signatures**: Ensures the authenticity and integrity of a message.
- **Key Exchange**: Securely exchanges keys for symmetric cryptography.

## References

- For more detailed information on RSA, see [IEEE Xplore](https://ieeexplore.ieee.org/) and [arXiv](https://arxiv.org/).
