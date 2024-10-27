
import numpy as np
from QuantumSigmoidCirq import quantum_sigmoid_cirq

def quantum_sigmoid_derivative_cirq(x):
    # Compute sigmoid value using quantum function
    sigmoid_value = quantum_sigmoid_cirq(x)

    # Compute derivative
    derivative = sigmoid_value * (1 - sigmoid_value)
    return derivative
