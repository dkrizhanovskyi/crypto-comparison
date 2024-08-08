import unittest
from qiskit import Aer, transpile, assemble, execute
from quantum_teleportation_example import quantum_teleportation

class TestQuantumTeleportationExample(unittest.TestCase):

    def test_quantum_teleportation(self):
        qc = quantum_teleportation()
        
        # Simulate the circuit
        backend = Aer.get_backend('qasm_simulator')
        tqc = transpile(qc, backend)
        qobj = assemble(tqc)
        result = execute(qc, backend).result()
        counts = result.get_counts()
        
        # Check if the result contains the expected teleportation outcome
        # |001> is the expected outcome for teleporting state |1> 
        self.assertIn('001', counts)
        self.assertGreater(counts['001'], 0)

if __name__ == '__main__':
    unittest.main()
