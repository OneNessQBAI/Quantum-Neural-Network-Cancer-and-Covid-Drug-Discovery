
import numpy as np
import cirq

def quantum_pool_layer_cirq(X, f, stride, mode):
    # Quantum implementation of the pooling layer
    # For demonstration, we simulate the pooling operation
    (n_C, n_H_prev, n_W_prev) = X.shape
    n_H = int(1 + (n_H_prev - f) / stride)
    n_W = int(1 + (n_W_prev - f) / stride)
    X_pool = np.zeros((n_C, n_H, n_W))

    for c in range(n_C):
        for h in range(n_H):
            for w in range(n_W):
                vert_start = h * stride
                vert_end = vert_start + f
                horiz_start = w * stride
                horiz_end = horiz_start + f

                X_slice = X[c, vert_start:vert_end, horiz_start:horiz_end]

                if mode == 'max':
                    # Simulate quantum max pooling
                    X_pool[c, h, w] = np.max(X_slice)
                elif mode == 'average':
                    # Simulate quantum average pooling
                    X_pool[c, h, w] = np.mean(X_slice)

    return X_pool
