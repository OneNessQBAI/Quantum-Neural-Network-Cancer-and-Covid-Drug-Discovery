import math

def tanh(x):
    return math.tanh(x)

# Piece 1: Exponentiation
def calculate_exponents(x):
    return math.exp(x), math.exp(-x)

# Piece 2: Subtraction
def subtract_exponents(exp_x, exp_neg_x):
    return exp_x - exp_neg_x

# Piece 3: Addition
def add_exponents(exp_x, exp_neg_x):
    return exp_x + exp_neg_x

# Piece 4: Division
def divide_results(sub_result, add_result):
    return sub_result / add_result

# Tolerance check for floating-point comparisons
def almost_equal(a, b, tol=1e-9):
    return abs(a - b) < tol

# Test function to compare piecewise and combined outputs
def test_tanh(input_value):
    exp_x, exp_neg_x = calculate_exponents(input_value)
    sub_result = subtract_exponents(exp_x, exp_neg_x)
    add_result = add_exponents(exp_x, exp_neg_x)
    output_piecewise = divide_results(sub_result, add_result)
    output_combined = tanh(input_value)
    return almost_equal(output_piecewise, output_combined), output_piecewise, output_combined

# Example usage
if __name__ == "__main__":
    test_values = [-5, 0, 5]
    for value in test_values:
        match, piecewise_output, combined_output = test_tanh(value)
        print(f"Input: {value}, Piecewise Output: {piecewise_output}, Combined Output: {combined_output}, Match: {match}")

