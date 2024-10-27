
import numpy as np
from QuantumSigmoidDerivativeCirq import quantum_sigmoid_derivative_cirq

def quantum_backward_pass_cirq(y, output, weights, layer_activations):
    # Calculate error
    error = y - output
    # Calculate delta for output layer
    delta_output = error * quantum_sigmoid_derivative_cirq(output)
    deltas = [delta_output]

    # Backpropagate through hidden layers
    for i in range(len(weights) - 1, 0, -1):
        error = deltas[-1] @ weights[i].T
        delta = error * quantum_sigmoid_derivative_cirq(layer_activations[i - 1])
        deltas.append(delta)

    deltas.reverse()
    return deltas
