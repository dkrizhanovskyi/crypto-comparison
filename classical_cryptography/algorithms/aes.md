# AES (Advanced Encryption Standard)

AES (Advanced Encryption Standard) is a symmetric encryption algorithm that is widely used for securing data. It was established as a standard by the U.S. National Institute of Standards and Technology (NIST) in 2001.

## How AES Works

AES operates on fixed block sizes of 128 bits and supports key sizes of 128, 192, or 256 bits. The algorithm consists of multiple rounds of processing, which vary depending on the key size:

- 10 rounds for 128-bit keys.
- 12 rounds for 192-bit keys.
- 14 rounds for 256-bit keys.

### Key Steps in AES Encryption

1. **Key Expansion**: The initial key is expanded into multiple round keys.

2. **Initial Round**:
   - AddRoundKey: Each byte of the state is combined with a block of the round key using bitwise XOR.

3. **Main Rounds**:
   - SubBytes: Each byte is replaced with its corresponding value from a substitution box (S-box).
   - ShiftRows: Rows of the state are shifted cyclically.
   - MixColumns: Columns of the state are mixed using a linear transformation.
   - AddRoundKey: Each byte of the state is combined with a block of the round key using bitwise XOR.

4. **Final Round** (without MixColumns):
   - SubBytes: Each byte is replaced with its corresponding value from a substitution box (S-box).
   - ShiftRows: Rows of the state are shifted cyclically.
   - AddRoundKey: Each byte of the state is combined with a block of the round key using bitwise XOR.

## Security

AES is considered secure against all known attacks when used with sufficient key length (128 bits or more). It is resistant to both linear and differential cryptanalysis.

## Applications

- **Data Encryption**: AES is used to encrypt data in transit and at rest.
- **Secure Communications**: Used in protocols like SSL/TLS and IPsec.
- **Storage Encryption**: Used to secure files and disk encryption.

## References

- For more detailed information on AES, see [IEEE Xplore](https://ieeexplore.ieee.org/) and [arXiv](https://arxiv.org/).
