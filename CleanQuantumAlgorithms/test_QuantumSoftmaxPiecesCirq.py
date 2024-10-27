```python
import numpy as np
from Softmax import softmax
from QuantumExponentiationCirq import quantum_exponentiation_cirq
from QuantumSummationCirq import quantum_summation_cirq
from QuantumDivisionCirq import quantum_division_cirq
from QuantumSoftmaxCirq import quantum_softmax_cirq

def test_softmax_pieces(x):
    # Classical computations
    exp_x_classical = np.exp(x)
    sum_exp_x_classical = np.sum(exp_x_classical)
    softmax_output_classical = exp_x_classical / sum_exp_x_classical

    # Quantum computations
    exp_x_quantum = quantum_exponentiation_cirq(x)
    sum_exp_x_quantum = quantum_summation_cirq(exp_x_quantum)
    softmax_output_quantum = quantum_division_cirq(exp_x_quantum, sum_exp_x_quantum)

    # Compare exponentiation
    match_exp = np.allclose(exp_x_classical, exp_x_quantum, atol=1e-6)
    print("Exponentiation Match:", match_exp)
    if not match_exp:
        print("Discrepancy in exponentiation step.")

    # Compare summation
    match_sum = np.isclose(sum_exp_x_classical, sum_exp_x_quantum, atol=1e-6)
    print("Summation Match:", match_sum)
    if not match_sum:
        print("Discrepancy in summation step.")

    # Compare division (Softmax output)
    match_softmax = np.allclose(softmax_output_classical, softmax_output_quantum, atol=1e-6)
    print("Softmax Output Match:", match_softmax)
    if not match_softmax:
        print("Discrepancy in softmax output.")

def test_softmax_function(x):
    # Classical softmax
    softmax_output_classical = softmax(x)

    # Quantum softmax
    softmax_output_quantum = quantum_softmax_cirq(x)

    # Compare outputs
    match_softmax = np.allclose(softmax_output_classical, softmax_output_quantum, atol=1e-6)
    print("Overall Softmax Function Match:", match_softmax)
    if not match_softmax:
        print("Discrepancy in overall softmax function.")

# Example usage
if __name__ == "__main__":
    x = np.array([1.0, 2.0, 3.0])  # Example input

    print("Testing Softmax Pieces:")
    test_softmax_pieces(x)
    print("\nTesting Overall Softmax Function:")
    test_softmax_function(x)
```