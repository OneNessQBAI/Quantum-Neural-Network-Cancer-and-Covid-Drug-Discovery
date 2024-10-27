import math
import numpy as np
from calculate_exponent import calculate_exponent
from add_one import add_one
from divide_one import divide_one

from QuantumCalculateExponentCirq import quantum_calculate_exponent_cirq
from QuantumAddOneCirq import quantum_add_one_cirq
from QuantumDivideOneCirq import quantum_divide_one_cirq

def test_pieces(input_value):
    # Classical computations
    exponent_result_classical = calculate_exponent(input_value)
    addition_result_classical = add_one(exponent_result_classical)
    output_piecewise_classical = divide_one(addition_result_classical)

    # Quantum computations
    exponent_result_quantum = quantum_calculate_exponent_cirq(input_value)
    addition_result_quantum = quantum_add_one_cirq(exponent_result_quantum)
    output_piecewise_quantum = quantum_divide_one_cirq(addition_result_quantum)

    # Compare results
    match_exponent = np.isclose(exponent_result_classical, exponent_result_quantum)
    match_addition = np.isclose(addition_result_classical, addition_result_quantum)
    match_division = np.isclose(output_piecewise_classical, output_piecewise_quantum)

    print(f"Input: {input_value}")
    print(f"Exponent Match: {match_exponent}")
    print(f"Addition Match: {match_addition}")
    print(f"Division Match: {match_division}")
    print(f"Classical Output: {output_piecewise_classical}")
    print(f"Quantum Output: {output_piecewise_quantum}\n")

    return match_exponent and match_addition and match_division

# Example usage
if __name__ == "__main__":
    test_values = [-5, 0, 5]
    for value in test_values:
        overall_match = test_pieces(value)
        print(f"Overall Match: {overall_match}\n")