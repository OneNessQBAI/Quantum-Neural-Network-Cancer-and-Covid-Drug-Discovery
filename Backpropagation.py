import numpy as np

# Sigmoid and its derivative
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# Backpropagation function
def backpropagation(X, y, weights, biases, learning_rate):
    # Forward pass
    layer_input = X
    layer_activations = []
    
    for w, b in zip(weights, biases):
        layer_input = sigmoid(np.dot(layer_input, w) + b)
        layer_activations.append(layer_input)
    
    output = layer_input
    
    # Backward pass
    error = y - output
    deltas = [error * sigmoid_derivative(output)]
    
    for i in range(len(weights) - 1, 0, -1):
        error = deltas[-1].dot(weights[i].T)
        delta = error * sigmoid_derivative(layer_activations[i - 1])
        deltas.append(delta)
    
    deltas.reverse()
    
    # Update weights and biases
    input_to_layer = X
    for i in range(len(weights)):
        weights[i] += input_to_layer.T.dot(deltas[i]) * learning_rate
        biases[i] += np.sum(deltas[i], axis=0, keepdims=True) * learning_rate
        input_to_layer = layer_activations[i]
    
    return weights, biases

# Piece 2: Forward Pass Calculations
def forward_pass(X, weights, biases):
    layer_input = X
    layer_activations = []
    
    for w, b in zip(weights, biases):
        layer_input = sigmoid(np.dot(layer_input, w) + b)
        layer_activations.append(layer_input)
    
    return layer_activations

# Piece 3: Backward Pass Calculations
def backward_pass(y, output, weights, layer_activations):
    error = y - output
    deltas = [error * sigmoid_derivative(output)]
    
    for i in range(len(weights) - 1, 0, -1):
        error = deltas[-1].dot(weights[i].T)
        delta = error * sigmoid_derivative(layer_activations[i - 1])
        deltas.append(delta)
    
    deltas.reverse()
    
    return deltas

# Piece 4: Update Weights and Biases
def update_weights_biases(X, weights, biases, deltas, layer_activations, learning_rate):
    input_to_layer = X
    for i in range(len(weights)):
        weights[i] += input_to_layer.T.dot(deltas[i]) * learning_rate
        biases[i] += np.sum(deltas[i], axis=0, keepdims=True) * learning_rate
        input_to_layer = layer_activations[i]
    
    return weights, biases

# Test function to combine and verify
def test_backpropagation(X, y, weights, biases, learning_rate):
    # Forward pass
    layer_activations = forward_pass(X, weights, biases)
    output = layer_activations[-1]

    # Backward pass
    deltas = backward_pass(y, output, weights, layer_activations)

    # Update weights and biases
    new_weights, new_biases = update_weights_biases(X, weights, biases, deltas, layer_activations, learning_rate)
    
    return new_weights, new_biases

# Example usage
if __name__ == "__main__":
    X = np.array([[0.1, 0.2, 0.3]])  # Example input
    y = np.array([[1]])  # Example expected output
    weights = [np.random.rand(3, 4), np.random.rand(4, 1)]  # Example weights
    biases = [np.random.rand(4), np.random.rand(1)]  # Example biases
    learning_rate = 0.01  # Example learning rate
    new_weights, new_biases = test_backpropagation(X, y, weights, biases, learning_rate)
    print(f"Updated Weights: {new_weights}")
    print(f"Updated Biases: {new_biases}")
