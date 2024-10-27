
import numpy as np
from Sigmoid import sigmoid
from QuantumSigmoidCirq import quantum_sigmoid

inputs = np.linspace(-6, 6, 25)
tolerance = 0.01  # Acceptable tolerance level

for x in inputs:
    classical_output = sigmoid(x)
    quantum_output = quantum_sigmoid(x)
    match = np.isclose(classical_output, quantum_output, atol=tolerance)
    print(f"Input: {x:.2f}, Classical Sigmoid Output: {classical_output:.5f}, Quantum Sigmoid Output: {quantum_output:.5f}, Match: {match}")
    if not match:
        print("The outputs do not match within the tolerance!")