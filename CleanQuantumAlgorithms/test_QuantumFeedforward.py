```python
import numpy as np
from Feedforward import feedforward
from QuantumFeedforward import quantum_feedforward_cirq

def test_feedforward(inputs, weights, biases):
    # Classical computation
    output_classical = feedforward(inputs, weights, biases)
    # Quantum computation
    output_quantum = quantum_feedforward_cirq(inputs, weights, biases)
    # Compare outputs
    match = np.allclose(output_classical, output_quantum, atol=0.1)
    print(f"Classical Output: {output_classical}")
    print(f"Quantum Output: {output_quantum}")
    print(f"Match: {match}")
    return match

# Example usage
if __name__ == "__main__":
    inputs = np.array([[0.1, 0.2, 0.3]])  # Example input
    weights = [np.random.rand(3, 4), np.random.rand(4, 2)]  # Example weights
    biases = [np.random.rand(4), np.random.rand(2)]  # Example biases
    test_feedforward(inputs, weights, biases)
```