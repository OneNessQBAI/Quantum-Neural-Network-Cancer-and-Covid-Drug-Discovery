
import numpy as np
from QuantumApplyActivationCirq import quantum_apply_activation_cirq
from QuantumCalculateLayerInputCirq import quantum_calculate_layer_input_cirq
from QuantumSigmoidCirq import quantum_sigmoid_cirq

def quantum_forward_pass_cirq(X, weights, biases):
    layer_input = X
    layer_activations = []

    for w, b in zip(weights, biases):
        # Calculate layer input
        layer_input_quantum = quantum_calculate_layer_input_cirq(layer_input, w, b)
        # Apply activation function
        activation_quantum = quantum_apply_activation_cirq(layer_input_quantum)
        layer_activations.append(activation_quantum)
        layer_input = activation_quantum

    return layer_activations
