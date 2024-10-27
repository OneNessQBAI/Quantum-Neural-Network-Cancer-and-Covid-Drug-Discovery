
import numpy as np
from Feedforward import calculate_layer_input, apply_activation, update_layer_input
from QuantumCalculateLayerInputCirq import quantum_calculate_layer_input_cirq
from QuantumApplyActivationCirq import quantum_apply_activation_cirq
from QuantumUpdateLayerInputCirq import quantum_update_layer_input_cirq

def test_feedforward_pieces(inputs, weights, biases):
    # Test each piece individually and compare outputs
    layer_input = inputs

    for idx, (w, b) in enumerate(zip(weights, biases)):
        print(f"Testing Layer {idx + 1}")

        # Classical calculations
        layer_input_classical = calculate_layer_input(layer_input, w, b)
        activation_classical = apply_activation(layer_input_classical)
        layer_input_classical = update_layer_input(activation_classical)

        # Quantum calculations
        layer_input_quantum = quantum_calculate_layer_input_cirq(layer_input, w, b)
        activation_quantum = quantum_apply_activation_cirq(layer_input_quantum)
        layer_input_quantum = quantum_update_layer_input_cirq(activation_quantum)

        # Compare Calculate Layer Input
        match_input = np.allclose(layer_input_classical, layer_input_quantum, atol=1e-6)
        print(f"Calculate Layer Input Match: {match_input}")

        # Compare Activation Output
        match_activation = np.allclose(activation_classical, activation_quantum, atol=0.1)
        print(f"Apply Activation Match: {match_activation}")

        # Update layer input for next iteration
        layer_input = layer_input_quantum

        if not match_input or not match_activation:
            print("Discrepancy found in Layer", idx + 1)
        else:
            print("Layer", idx + 1, "matches successfully")
        print("-" * 50)

# Example usage
if __name__ == "__main__":
    inputs = np.array([[0.1, 0.2, 0.3]])
    weights = [np.random.rand(3, 4), np.random.rand(4, 2)]
    biases = [np.random.rand(1, 4), np.random.rand(1, 2)]
    test_feedforward_pieces(inputs, weights, biases)
