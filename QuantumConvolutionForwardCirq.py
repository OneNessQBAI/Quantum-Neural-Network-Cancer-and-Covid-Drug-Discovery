
import numpy as np
import cirq
from QuantumPadInputCirq import quantum_pad_input_cirq
from QuantumComputeConvolutionCirq import quantum_compute_convolution_cirq

def quantum_convolution_forward_cirq(X, W, b, stride=1, padding=0):
    (n_C_prev, n_H_prev, n_W_prev) = X.shape
    (n_C, n_C_prev, f, f) = W.shape

    n_H = int((n_H_prev - f + 2 * padding) / stride) + 1
    n_W = int((n_W_prev - f + 2 * padding) / stride) + 1

    X_pad = quantum_pad_input_cirq(X, padding)
    Z = quantum_compute_convolution_cirq(X_pad, W, b, stride, n_H, n_W, n_C, f)

    return Z
