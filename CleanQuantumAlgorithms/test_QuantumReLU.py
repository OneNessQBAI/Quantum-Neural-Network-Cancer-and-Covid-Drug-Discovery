import numpy as np
from ReLU import relu
from QuantumReLU import quantum_relu

inputs = np.linspace(-10, 10, 21)
tolerance = 0.1  # Set acceptable tolerance level

for x in inputs:
    classical_output = relu(x)
    quantum_output = quantum_relu(x)
    match = np.isclose(classical_output, quantum_output, atol=tolerance)
    print(f"Input: {x:.2f}, Classical ReLU Output: {classical_output:.5f}, Quantum ReLU Output: {quantum_output:.5f}, Match: {match}")

    if not match:
        print("The outputs do not match within the tolerance!")