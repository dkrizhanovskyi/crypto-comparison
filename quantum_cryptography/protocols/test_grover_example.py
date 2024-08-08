import unittest
from qiskit import Aer, transpile, assemble, execute
from grover_example import grover_algorithm

class TestGroverExample(unittest.TestCase):

    def test_grover_algorithm(self):
        n = 3  # Number of qubits
        qc = grover_algorithm(n)
        
        # Simulate the circuit
        backend = Aer.get_backend('qasm_simulator')
        tqc = transpile(qc, backend)
        qobj = assemble(tqc)
        result = execute(qc, backend).result()
        counts = result.get_counts()
        
        # Check if the result contains the expected solution
        self.assertIn('001', counts)
        self.assertGreater(counts['001'], 0)

if __name__ == '__main__':
    unittest.main()

