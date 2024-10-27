
import numpy as np
import cirq

def quantum_pool_gradients_cirq(dX_pool, X, f, stride, mode):
    # Quantum implementation of pooling gradients
    # For demonstration, we simulate the gradient computation
    (n_C, n_H_prev, n_W_prev) = X.shape
    n_H = int(1 + (n_H_prev - f) / stride)
    n_W = int(1 + (n_W_prev - f) / stride)
    dX = np.zeros(X.shape)

    for c in range(n_C):
        for h in range(n_H):
            for w in range(n_W):
                vert_start = h * stride
                vert_end = vert_start + f
                horiz_start = w * stride
                horiz_end = horiz_start + f

                X_slice = X[c, vert_start:vert_end, horiz_start:horiz_end]

                if mode == 'max':
                    mask = (X_slice == np.max(X_slice))
                    dX[c, vert_start:vert_end, horiz_start:horiz_end] += mask * dX_pool[c, h, w]
                elif mode == 'average':
                    da = dX_pool[c, h, w]
                    shape = (f, f)
                    dX[c, vert_start:vert_end, horiz_start:horiz_end] += np.ones(shape) * da / (f * f)

    return dX
