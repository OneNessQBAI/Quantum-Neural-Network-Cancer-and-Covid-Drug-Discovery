import numpy as np
from qiskit import QuantumCircuit, Aer, execute

def quantum_relu(x):
    # For x <= 0, return 0 directly
    if x <= 0:
        return 0.0

    # Normalize x to [0, pi/2], assuming x in [0, 10] for this example
    x_max = 10  # Modify x_max based on the expected input range
    normalized_x = (x / x_max) * (np.pi / 2)

    # Initialize quantum circuit with one qubit
    qc = QuantumCircuit(1, 1)
    qc.ry(2 * normalized_x, 0)  # Rotate qubit based on normalized input
    qc.measure(0, 0)

    # Execute the circuit
    backend = Aer.get_backend('qasm_simulator')
    job = execute(qc, backend, shots=8192)
    result = job.result()
    counts = result.get_counts()

    # Probability of measuring '1'
    prob_one = counts.get('1', 0) / 8192

    # Scale the probability back to the original range
    relu_output = prob_one * x_max

    return relu_output