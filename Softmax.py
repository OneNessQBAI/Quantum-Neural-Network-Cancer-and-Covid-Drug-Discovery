import numpy as np

# Piece 1: Softmax Forward Calculations

def compute_softmax(Z):
    exp_Z = np.exp(Z - np.max(Z))
    return exp_Z / exp_Z.sum(axis=1, keepdims=True)

# Piece 2: Softmax Forward (Wrapper Function)

def softmax(Z):
    return compute_softmax(Z)

# Piece 3: Softmax Backward Calculations

def compute_softmax_gradients(dA, Z):
    s = softmax(Z)
    dZ = dA * s * (1 - s)
    return dZ

# Piece 4: Softmax Backward (Wrapper Function)

def softmax_backward(dA, Z):
    return compute_softmax_gradients(dA, Z)

# Test function to combine and verify

def test_softmax(Z, dA):
    A = softmax(Z)
    dZ = softmax_backward(dA, Z)
    
    return A, dZ

# Example usage
if __name__ == "__main__":
    Z = np.random.rand(3, 5)  # Example input
    dA = np.random.rand(3, 5)  # Example gradient w.r.t. output
    A, dZ = test_softmax(Z, dA)
    print(f"Softmax Output (A): {A}")
    print(f"Gradient w.r.t. input (dZ): {dZ}")
