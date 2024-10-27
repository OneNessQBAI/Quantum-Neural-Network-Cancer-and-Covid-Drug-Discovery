
import numpy as np

def quantum_update_weights_biases_cirq(X, weights, biases, deltas, layer_activations, learning_rate):
    input_to_layer = X
    for i in range(len(weights)):
        weights[i] += input_to_layer.T @ deltas[i] * learning_rate
        biases[i] += np.sum(deltas[i], axis=0, keepdims=True) * learning_rate
        input_to_layer = layer_activations[i]
    return weights, biases
