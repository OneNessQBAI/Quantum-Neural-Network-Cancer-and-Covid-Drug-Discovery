import math
import numpy as np
from calculate_exponent import calculate_exponent # type: ignore
from QuantumCalculateExponent import quantum_calculate_exponent
from add_one import add_one # type: ignore
from QuantumAddOne import quantum_add_one
from divide_one import divide_one # type: ignore
from QuantumDivideOne import quantum_divide_one

def test_pieces(input_value):
    # Classical computations
    exponent_result_classical = calculate_exponent(input_value)
    addition_result_classical = add_one(exponent_result_classical)
    output_piecewise_classical = divide_one(addition_result_classical)

    # Quantum computations
    exponent_result_quantum = quantum_calculate_exponent(input_value)
    addition_result_quantum = quantum_add_one(exponent_result_quantum)
    output_piecewise_quantum = quantum_divide_one(addition_result_quantum)

    # Compare results
    match_exponent = np.isclose(exponent_result_classical, exponent_result_quantum, atol=1e-2)
    match_addition = np.isclose(addition_result_classical, addition_result_quantum, atol=1e-2)
    match_division = np.isclose(output_piecewise_classical, output_piecewise_quantum, atol=1e-2)

    print(f"Input: {input_value}")
    print(f"Exponent Match: {match_exponent}")
    print(f"Addition Match: {match_addition}")
    print(f"Division Match: {match_division}")
    print(f"Classical Output: {output_piecewise_classical}")
    print(f"Quantum Output: {output_piecewise_quantum}")

    return (match_exponent and match_addition and match_division)

# Example usage
if __name__ == "__main__":
    test_values = [-5, 0, 5]
    for value in test_values:
        match = test_pieces(value)
        print(f"Overall Match: {match}")