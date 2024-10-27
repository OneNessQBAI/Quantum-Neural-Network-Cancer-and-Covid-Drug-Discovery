import numpy as np

# Piece 1: Padding and Convolution Calculations (Forward Pass)

def pad_input(X, padding):
    return np.pad(X, ((0, 0), (padding, padding), (padding, padding)), 'constant', constant_values=0)


def compute_convolution(X_pad, W, b, stride, n_H, n_W, n_C, f):
    Z = np.zeros((n_C, n_H, n_W))

    for h in range(n_H):
        for w in range(n_W):
            for c in range(n_C):
                vert_start = h * stride
                vert_end = vert_start + f
                horiz_start = w * stride
                horiz_end = horiz_start + f

                X_slice = X_pad[:, vert_start:vert_end, horiz_start:horiz_end]
                Z[c, h, w] = np.sum(X_slice * W[c, :, :, :]) + b[c]

    return Z

# Piece 2: Convolution Forward (Combining Padding and Convolution)

def convolution_forward(X, W, b, stride=1, padding=0):
    (n_C_prev, n_H_prev, n_W_prev) = X.shape
    (n_C, n_C_prev, f, f) = W.shape

    n_H = int((n_H_prev - f + 2 * padding) / stride) + 1
    n_W = int((n_W_prev - f + 2 * padding) / stride) + 1

    X_pad = pad_input(X, padding)
    Z = compute_convolution(X_pad, W, b, stride, n_H, n_W, n_C, f)

    return Z

# Piece 3: Compute Gradients (Backward Pass)

def compute_grads(dZ, X_pad, W, stride, n_H, n_W, n_C, f, padding):
    dX = np.zeros(X_pad.shape)
    dW = np.zeros(W.shape)
    db = np.zeros((n_C, 1))

    for h in range(n_H):
        for w in range(n_W):
            for c in range(n_C):
                vert_start = h * stride
                vert_end = vert_start + f
                horiz_start = w * stride
                horiz_end = horiz_start + f

                dX[:, vert_start:vert_end, horiz_start:horiz_end] += W[c, :, :, :] * dZ[c, h, w]
                dW[c, :, :, :] += X_pad[:, vert_start:vert_end, horiz_start:horiz_end] * dZ[c, h, w]
                db[c] += dZ[c, h, w]

    if padding > 0:
        dX = dX[:, padding:-padding, padding:-padding]

    return dX, dW, db

# Piece 4: Convolution Backward (Combining Gradient Computation and Padding)

def convolution_backward(dZ, X, W, stride=1, padding=0):
    X_pad = pad_input(X, padding)
    dX, dW, db = compute_grads(dZ, X_pad, W, stride, dZ.shape[1], dZ.shape[2], W.shape[0], W.shape[2], padding)

    return dX, dW, db

# Test function to combine and verify

def test_convolution(X, W, b, dZ, stride=1, padding=0):
    Z = convolution_forward(X, W, b, stride, padding)
    dX, dW, db = convolution_backward(dZ, X, W, stride, padding)

    return Z, dX, dW, db

# Example usage
if __name__ == "__main__":
    X = np.random.rand(3, 10, 10)  # Example input of shape (n_C_prev, n_H_prev, n_W_prev)
    W = np.random.rand(8, 3, 3, 3)  # Example weights of shape (n_C, n_C_prev, f, f)
    b = np.random.rand(8)  # Example biases
    dZ = np.random.rand(8, 8, 8)  # Example gradient w.r.t. output
    stride = 1
    padding = 1
    Z, dX, dW, db = test_convolution(X, W, b, dZ, stride, padding)
    print(f"Output (Z): {Z}")
    print(f"Gradient w.r.t. input (dX): {dX}")
    print(f"Gradient w.r.t. weights (dW): {dW}")
    print(f"Gradient w.r.t. biases (db): {db}")
