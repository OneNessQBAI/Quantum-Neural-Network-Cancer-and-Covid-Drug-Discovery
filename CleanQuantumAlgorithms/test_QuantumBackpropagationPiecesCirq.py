```python
import numpy as np
from Backpropagation import forward_pass, backward_pass, update_weights_biases
from QuantumForwardPassCirq import quantum_forward_pass_cirq
from QuantumBackwardPassCirq import quantum_backward_pass_cirq
from QuantumUpdateWeightsBiasesCirq import quantum_update_weights_biases_cirq

def test_backpropagation_pieces(X, y, weights, biases, learning_rate):
    # Classical computations
    layer_activations_classical = forward_pass(X, weights, biases)
    output_classical = layer_activations_classical[-1]

    deltas_classical = backward_pass(y, output_classical, weights, layer_activations_classical)
    new_weights_classical, new_biases_classical = update_weights_biases(
        X, [w.copy() for w in weights], [b.copy() for b in biases],
        deltas_classical, layer_activations_classical, learning_rate)

    # Quantum computations
    layer_activations_quantum = quantum_forward_pass_cirq(X, weights, biases)
    output_quantum = layer_activations_quantum[-1]

    deltas_quantum = quantum_backward_pass_cirq(y, output_quantum, weights, layer_activations_quantum)
    new_weights_quantum, new_biases_quantum = quantum_update_weights_biases_cirq(
        X, [w.copy() for w in weights], [b.copy() for b in biases],
        deltas_quantum, layer_activations_quantum, learning_rate)

    # Compare outputs
    match_forward = np.allclose(output_classical, output_quantum, atol=1e-2)
    match_backward = all(np.allclose(dc, dq, atol=1e-2) for dc, dq in zip(deltas_classical, deltas_quantum))
    match_weights = all(np.allclose(wc, wq, atol=1e-2) for wc, wq in zip(new_weights_classical, new_weights_quantum))
    match_biases = all(np.allclose(bc, bq, atol=1e-2) for bc, bq in zip(new_biases_classical, new_biases_quantum))

    print("Forward Pass Match:", match_forward)
    print("Backward Pass Match:", match_backward)
    print("Weights Update Match:", match_weights)
    print("Biases Update Match:", match_biases)

    if not match_forward:
        print("Discrepancy in forward pass outputs.")
    if not match_backward:
        print("Discrepancy in backward pass deltas.")
    if not match_weights:
        print("Discrepancy in updated weights.")
    if not match_biases:
        print("Discrepancy in updated biases.")

# Example usage
if __name__ == "__main__":
    X = np.array([[0.1, 0.2, 0.3]])  # Example input
    y = np.array([[1]])              # Example expected output
    weights = [np.random.rand(3, 4), np.random.rand(4, 1)]  # Example weights
    biases = [np.random.rand(1, 4), np.random.rand(1, 1)]   # Example biases
    learning_rate = 0.01
    test_backpropagation_pieces(X, y, weights, biases, learning_rate)
```