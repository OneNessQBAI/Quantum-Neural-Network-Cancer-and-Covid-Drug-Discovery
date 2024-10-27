import numpy as np

# Piece 1: Gradient Descent Procedure

def train_gradient_descent(X, y, weights, biases, learning_rate, epochs):
    for epoch in range(epochs):
        output = predict(X, weights, biases)
        dW, db = compute_gradients(X, y, output)  # Ensure this returns correct shapes
        weights, biases = update_parameters(weights, biases, dW, db, learning_rate)
    return weights, biases

# Piece 2: Prediction Function

def predict(X, weights, biases):
    layer_input = X
    for w, b in zip(weights, biases):
        layer_input = np.dot(layer_input, w) + b
    return layer_input

# Piece 3: Compute Gradients

def compute_gradients(X, y, output):
    error = y - output
    dW = [np.dot(X.T, error)]  # Placeholder - dimensions need to match exactly
    db = [np.sum(error, axis=0)]  # Placeholder
    return dW, db

# Piece 4: Update Parameters

def update_parameters(weights, biases, dW, db, learning_rate):
    for j in range(len(weights)):
        if j < len(dW) and j < len(biases):  # Ensure indexes match
            weights[j] -= learning_rate * dW[j]
            biases[j] -= learning_rate * db[j]
    return weights, biases

# Test function to combine and verify

def test_gradient_descent(X, y, weights, biases, learning_rate, epochs):
    final_weights, final_biases = train_gradient_descent(X, y, weights, biases, learning_rate, epochs)
    return final_weights, final_biases

# Example usage
if __name__ == "__main__":
    X = np.random.rand(10, 3)  # Example input
    y = np.random.rand(10, 1)  # Example expected output
    weights = [np.random.rand(3, 4), np.random.rand(4, 1)]  # Example weights
    biases = [np.random.rand(4), np.random.rand(1)]  # Example biases
    learning_rate = 0.01  # Example learning rate
    epochs = 100  # Number of epochs
    final_weights, final_biases = test_gradient_descent(X, y, weights, biases, learning_rate, epochs)
    print(f"Final Weights: {final_weights}")
    print(f"Final Biases: {final_biases}")

