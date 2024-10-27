import numpy as np

# Piece 1: Dropout Forward Calculations

def apply_dropout(X, dropout_rate):
    mask = np.random.rand(*X.shape) < (1 - dropout_rate)
    out = X * mask / (1 - dropout_rate)  # Scale the output
    return out, mask

# Piece 2: Dropout Backward Calculations

def apply_dropout_back(dout, mask, dropout_rate):
    return dout * mask / (1 - dropout_rate)  # Scale the gradient

# Test function to combine and verify

def test_dropout(X, dropout_rate):
    out, mask = apply_dropout(X, dropout_rate)
    dout = np.random.rand(*out.shape)  # Example gradient coming from the next layer
    dX = apply_dropout_back(dout, mask, dropout_rate)
    
    return out, dX

# Example usage
if __name__ == "__main__":
    X = np.random.rand(3, 5)  # Example input
    dropout_rate = 0.5  # Example dropout rate
    out, dX = test_dropout(X, dropout_rate)
    print(f"Output after dropout: {out}")
    print(f"Gradient w.r.t. input after dropout: {dX}")
