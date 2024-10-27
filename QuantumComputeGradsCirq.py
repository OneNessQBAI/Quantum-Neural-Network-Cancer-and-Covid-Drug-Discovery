
import numpy as np
import cirq

def quantum_compute_grads_cirq(dZ, X_pad, W, stride, n_H, n_W, n_C, f, padding):
    # Quantum implementation of computing gradients
    # For demonstration purposes, we simulate this step
    dX = np.zeros(X_pad.shape)
    dW = np.zeros(W.shape)
    db = np.zeros((n_C, 1))

    for c in range(n_C):
        for h in range(n_H):
            for w in range(n_W):
                # Define the corners of the current "slice"
                vert_start = h * stride
                vert_end = vert_start + f
                horiz_start = w * stride
                horiz_end = horiz_start + f

                # Compute gradients
                X_slice = X_pad[:, vert_start:vert_end, horiz_start:horiz_end]

                dX[:, vert_start:vert_end, horiz_start:horiz_end] += W[c, :, :, :] * dZ[c, h, w]
                dW[c, :, :, :] += X_slice * dZ[c, h, w]
                db[c] += dZ[c, h, w]

    if padding > 0:
        dX = dX[:, padding:-padding, padding:-padding]

    return dX, dW, db
