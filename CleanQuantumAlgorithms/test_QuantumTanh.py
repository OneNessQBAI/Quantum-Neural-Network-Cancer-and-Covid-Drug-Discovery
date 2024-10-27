import numpy as np
from Tanh import tanh
from QuantumTanh import quantum_tanh

inputs = np.linspace(-5, 5, 21)
tolerance = 0.05  # Set acceptable tolerance level

for x in inputs:
    classical_output = tanh(x)
    quantum_output = quantum_tanh(x)
    match = np.isclose(classical_output, quantum_output, atol=tolerance)
    print(f"Input: {x:.2f}, Classical Tanh Output: {classical_output:.5f}, Quantum Tanh Output: {quantum_output:.5f}, Match: {match}")
    if not match:
        print("The outputs do not match within the tolerance!")