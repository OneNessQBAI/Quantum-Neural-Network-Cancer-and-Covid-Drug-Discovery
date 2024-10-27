import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Feedforward function
def feedforward(inputs, weights, biases):
    layer_input = inputs
    for w, b in zip(weights, biases):
        layer_output = sigmoid(np.dot(layer_input, w) + b)
        layer_input = layer_output
    return layer_output

# Piece 1: Calculate Layer Input
def calculate_layer_input(inputs, weights, biases):
    return np.dot(inputs, weights) + biases

# Piece 2: Apply Activation Function
def apply_activation(layer_input):
    return sigmoid(layer_input)

# Piece 3: Update Layer Input
def update_layer_input(previous_output):
    return previous_output

# Test function to compare piecewise and combined outputs
def test_feedforward(inputs, weights, biases):
    layer_input = inputs
    for w, b in zip(weights, biases):
        layer_input_calculated = calculate_layer_input(layer_input, w, b)
        layer_output_calculated = apply_activation(layer_input_calculated)
        layer_input = update_layer_input(layer_output_calculated)
    output_piecewise = layer_input
    output_combined = feedforward(inputs, weights, biases)
    return (np.allclose(output_piecewise, output_combined), output_piecewise, output_combined)

# Example usage
if __name__ == "__main__":
    inputs = np.array([[0.1, 0.2, 0.3]])  # Example input
    weights = [np.random.rand(3, 4), np.random.rand(4, 2)]  # Example weights
    biases = [np.random.rand(4), np.random.rand(2)]  # Example biases
    match, piecewise_output, combined_output = test_feedforward(inputs, weights, biases)
    print(f"Piecewise Output: {piecewise_output}")
    print(f"Combined Output: {combined_output}")
    print(f"Match: {match}")
