from qiskit import QuantumCircuit, Aer, transpile, assemble, execute
from qiskit.visualization import plot_histogram
from qiskit.circuit.library import GroverOperator
from qiskit.algorithms import AmplificationProblem

# Define the oracle for the problem
def oracle(circuit, n):
    circuit.cz(0, n-1)
    circuit.h(0)

# Grover's algorithm
def grover_algorithm(n):
    # Create quantum and classical registers
    qc = QuantumCircuit(n)
    
    # Apply Hadamard gates
    qc.h(range(n))
    
    # Apply the oracle
    oracle(qc, n)
    
    # Apply the Grover diffusion operator
    grover_op = GroverOperator(qc)
    qc.append(grover_op, range(n))
    
    # Measure the qubits
    qc.measure_all()
    
    return qc

# Example usage
n = 3  # Number of qubits
qc = grover_algorithm(n)
qc.draw('mpl')

# Simulate the circuit
backend = Aer.get_backend('qasm_simulator')
tqc = transpile(qc, backend)
qobj = assemble(tqc)
result = execute(qc, backend).result()
counts = result.get_counts()

# Plot the results
plot_histogram(counts)
