# Installation Guide

This document provides step-by-step instructions for setting up the environment and installing the dependencies required to run the examples and tests in the Crypto Comparison Project.

## Prerequisites

Ensure that you have the following software installed on your system:

- Python 3.7 or higher
- Git

## Cloning the Repository

First, clone the repository to your local machine:

```sh
git clone https://github.com/dkrizhanovskyi/crypto-comparison.git
cd crypto-comparison
```

## Setting Up a Virtual Environment

It's recommended to create a virtual environment to manage dependencies. Run the following commands to create and activate a virtual environment:

```sh
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

## Installing Dependencies

Install the required Python packages using `pip`:

```sh
pip install -r requirements.txt
```

The `requirements.txt` file should include the following packages:

```txt
qiskit
pycryptodome
```

## Running Examples

To run the example scripts, navigate to the corresponding directory and execute the script:

```sh
python classical_cryptography/algorithms/rsa_example.py
python classical_cryptography/algorithms/aes_example.py
python classical_cryptography/algorithms/ecc_example.py
python quantum_cryptography/protocols/qkd_example.py
python quantum_cryptography/protocols/bb84_example.py
python quantum_cryptography/protocols/grover_example.py
python quantum_cryptography/protocols/quantum_teleportation_example.py
python quantum_cryptography/protocols/quantum_encryption_example.py
python quantum_cryptography/protocols/quantum_superposition_entanglement_example.py
```

## Running Tests

To run the tests, use the following command:

```sh
python -m unittest discover
```

This command will discover and run all test cases in the repository.

## Additional Resources

- [Qiskit Documentation](https://qiskit.org/documentation/)
- [PyCryptodome Documentation](https://www.pycryptodome.org/src/installation)

If you encounter any issues during installation or setup, please open an issue on GitHub.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE.md) file for details.
