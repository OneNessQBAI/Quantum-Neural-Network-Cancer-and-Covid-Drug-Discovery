def relu(x):
    return max(0, x)

# Piece 1: Input Check
def is_negative(x):
    return x < 0

# Piece 2: Output Derivation
def relu_output(x, is_neg):
    if is_neg:
        return 0
    else:
        return x

# Test function to compare piecewise and combined outputs
def test_relu(input_value):
    neg_check = is_negative(input_value)
    output_piecewise = relu_output(input_value, neg_check)
    output_combined = relu(input_value)
    return output_piecewise == output_combined, output_piecewise, output_combined

# Example usage
if __name__ == "__main__":
    test_values = [-5, 0, 5]
    for value in test_values:
        match, piecewise_output, combined_output = test_relu(value)
        print(f"Input: {value}, Piecewise Output: {piecewise_output}, Combined Output: {combined_output}, Match: {match}")
