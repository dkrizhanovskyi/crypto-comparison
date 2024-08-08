import unittest
from qiskit import Aer, transpile, assemble, execute
from quantum_encryption_example import quantum_encryption

class TestQuantumEncryptionExample(unittest.TestCase):

    def test_quantum_encryption(self):
        qc = quantum_encryption()
        
        # Simulate the circuit
        backend = Aer.get_backend('qasm_simulator')
        tqc = transpile(qc, backend)
        qobj = assemble(tqc)
        result = execute(qc, backend).result()
        counts = result.get_counts()
        
        # Check if the result contains the expected encrypted outcome
        # Here, we assume '010' is the expected outcome for the superposition state encryption
        self.assertIn('010', counts)
        self.assertGreater(counts['010'], 0)

if __name__ == '__main__':
    unittest.main()
