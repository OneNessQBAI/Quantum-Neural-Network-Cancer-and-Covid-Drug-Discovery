import math

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

# Piece 1: Exponentiation
def calculate_exponent(x):
    return math.exp(-x)

# Piece 2: Addition
def add_one(exponent_result):
    return 1 + exponent_result

# Piece 3: Division
def divide_one(addition_result):
    return 1 / addition_result

# Test function to compare piecewise and combined outputs
def test_sigmoid(input_value):
    exponent_result = calculate_exponent(input_value)
    addition_result = add_one(exponent_result)
    output_piecewise = divide_one(addition_result)
    output_combined = sigmoid(input_value)
    return output_piecewise == output_combined, output_piecewise, output_combined

# Example usage
if __name__ == "__main__":
    test_values = [-5, 0, 5]
    for value in test_values:
        match, piecewise_output, combined_output = test_sigmoid(value)
        print(f"Input: {value}, Piecewise Output: {piecewise_output}, Combined Output: {combined_output}, Match: {match}")
