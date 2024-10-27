import numpy as np
from qiskit import QuantumCircuit, Aer, execute

def quantum_tanh(x):
    # Normalize x to [-pi/2, pi/2], assuming x in [-5, 5]
    x_max = 5
    normalized_x = (x / x_max) * (np.pi / 2)
    
    # Initialize quantum circuit with one qubit
    qc = QuantumCircuit(1, 1)
    qc.rx(2 * normalized_x, 0)  # Rotate around X-axis based on normalized input
    qc.measure(0, 0)
    
    # Execute the circuit
    backend = Aer.get_backend('qasm_simulator')
    job = execute(qc, backend, shots=8192)
    result = job.result()
    counts = result.get_counts()
    
    # Calculate expectation value
    prob_zero = counts.get('0', 0) / 8192
    prob_one = counts.get('1', 0) / 8192
    expectation_value = prob_zero - prob_one  # Expectation value of Pauli-Z operator
    
    return expectation_value