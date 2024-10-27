```python
import numpy as np
from BatchNormalization import calculate_mean_variance, normalize_input, scale_and_shift
from QuantumCalculateMeanVarianceCirq import quantum_calculate_mean_variance_cirq
from QuantumNormalizeInputCirq import quantum_normalize_input_cirq
from QuantumScaleAndShiftCirq import quantum_scale_and_shift_cirq

def test_batch_normalization_pieces(X, gamma, beta, eps=1e-5):
    # Classical computations
    mean_classical, variance_classical = calculate_mean_variance(X, eps)
    X_normalized_classical = normalize_input(X, mean_classical, variance_classical, eps)
    output_classical = scale_and_shift(X_normalized_classical, gamma, beta)

    # Quantum computations
    mean_quantum, variance_quantum = quantum_calculate_mean_variance_cirq(X, eps)
    X_normalized_quantum = quantum_normalize_input_cirq(X, mean_quantum, variance_quantum, eps)
    output_quantum = quantum_scale_and_shift_cirq(X_normalized_quantum, gamma, beta)

    # Compare results
    match_mean = np.allclose(mean_classical, mean_quantum, atol=1e-6)
    match_variance = np.allclose(variance_classical, variance_quantum, atol=1e-6)
    match_normalized = np.allclose(X_normalized_classical, X_normalized_quantum, atol=1e-6)
    match_output = np.allclose(output_classical, output_quantum, atol=1e-6)

    print("Mean Match:", match_mean)
    print("Variance Match:", match_variance)
    print("Normalization Match:", match_normalized)
    print("Output Match:", match_output)

    if not match_mean:
        print("Discrepancy in mean calculation.")
    if not match_variance:
        print("Discrepancy in variance calculation.")
    if not match_normalized:
        print("Discrepancy in input normalization.")
    if not match_output:
        print("Discrepancy in scaling and shifting output.")

# Example usage
if __name__ == "__main__":
    X = np.array([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])  # Example input
    gamma = np.array([1, 1, 1])  # Example scale parameter
    beta = np.array([0, 0, 0])   # Example shift parameter
    test_batch_normalization_pieces(X, gamma, beta)
```