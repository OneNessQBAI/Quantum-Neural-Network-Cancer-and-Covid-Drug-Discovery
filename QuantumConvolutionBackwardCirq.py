
import numpy as np
import cirq
from QuantumPadInputCirq import quantum_pad_input_cirq
from QuantumComputeGradsCirq import quantum_compute_grads_cirq

def quantum_convolution_backward_cirq(dZ, X, W, stride=1, padding=0):
    X_pad = quantum_pad_input_cirq(X, padding)
    n_H = dZ.shape[1]
    n_W = dZ.shape[2]
    n_C = W.shape[0]
    f = W.shape[2]

    dX, dW, db = quantum_compute_grads_cirq(dZ, X_pad, W, stride, n_H, n_W, n_C, f, padding)

    return dX, dW, db
