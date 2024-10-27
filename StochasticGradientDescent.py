import numpy as np

# Piece 1: Training Procedure

def train_sgd(X, y, weights, biases, learning_rate, epochs):
    for epoch in range(epochs):
        for i in range(len(X)):
            output = predict(X[i], weights, biases)
            error = y[i] - output
            dW, db = compute_gradients(X[i], error, weights)
            weights, biases = update_parameters(weights, biases, dW, db, learning_rate)
    return weights, biases

# Piece 2: Prediction Function

def predict(x, weights, biases):
    layer_input = x
    for w, b in zip(weights, biases):
        layer_input = np.dot(layer_input, w) + b
    return layer_input

# Piece 3: Compute Gradients

def compute_gradients(x, error, weights):
    # This function needs to be implemented based on the model structure
    # Assuming a single layer for simplicity - adjust to your network design
    dW = [np.outer(x, error)]  # Placeholder
    db = [error]  # Placeholder
    return dW, db

# Piece 4: Update Parameters

def update_parameters(weights, biases, dW, db, learning_rate):
    for j in range(len(weights)):
        if j < len(dW) and j < len(biases):  # Ensure indexes match
            weights[j] += learning_rate * dW[j]
            biases[j] += learning_rate * db[j]
    return weights, biases

# Test function to combine and verify

def test_stochastic_gradient_descent(X, y, weights, biases, learning_rate, epochs):
    final_weights, final_biases = train_sgd(X, y, weights, biases, learning_rate, epochs)
    return final_weights, final_biases

# Example usage
if __name__ == "__main__":
    X = np.random.rand(10, 3)  # Example input
    y = np.random.rand(10, 1)  # Example expected output
    weights = [np.random.rand(3, 4), np.random.rand(4, 1)]  # Example weights
    biases = [np.random.rand(4), np.random.rand(1)]  # Example biases
    learning_rate = 0.01  # Example learning rate
    epochs = 100  # Number of epochs
    final_weights, final_biases = test_stochastic_gradient_descent(X, y, weights, biases, learning_rate, epochs)
    print(f"Final Weights: {final_weights}")
    print(f"Final Biases: {final_biases}")

