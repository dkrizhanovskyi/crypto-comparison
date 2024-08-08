from qiskit import QuantumCircuit, Aer, transpile, assemble, execute
from qiskit.visualization import plot_histogram

def quantum_superposition_entanglement():
    qc = QuantumCircuit(2, 2)

    # Create superposition on the first qubit
    qc.h(0)

    # Create entanglement between the first and second qubit
    qc.cx(0, 1)
    qc.barrier()

    # Measure both qubits
    qc.measure([0, 1], [0, 1])

    return qc

# Example usage
qc = quantum_superposition_entanglement()
qc.draw('mpl')

# Simulate the circuit
backend = Aer.get_backend('qasm_simulator')
tqc = transpile(qc, backend)
qobj = assemble(tqc)
result = execute(qc, backend).result()
counts = result.get_counts()

# Plot the results
plot_histogram(counts)
