```python
import numpy as np
from ConvolutionalLayersCnn import pad_input, compute_convolution, convolution_forward, compute_grads, convolution_backward
from QuantumPadInputCirq import quantum_pad_input_cirq
from QuantumComputeConvolutionCirq import quantum_compute_convolution_cirq
from QuantumConvolutionForwardCirq import quantum_convolution_forward_cirq
from QuantumComputeGradsCirq import quantum_compute_grads_cirq
from QuantumConvolutionBackwardCirq import quantum_convolution_backward_cirq

def test_convolution_pieces(X, W, b, dZ, stride=1, padding=0):
    # Test padding function
    X_pad_classical = pad_input(X, padding)
    X_pad_quantum = quantum_pad_input_cirq(X, padding)
    match_pad = np.allclose(X_pad_classical, X_pad_quantum, atol=1e-6)
    print("Padding Function Match:", match_pad)
    if not match_pad:
        print("Discrepancy in padding function.")

    # Test compute_convolution function
    (n_C, n_C_prev, f, f) = W.shape
    n_H = int((X.shape[1] - f + 2 * padding) / stride) + 1
    n_W = int((X.shape[2] - f + 2 * padding) / stride) + 1

    Z_classical = compute_convolution(X_pad_classical, W, b, stride, n_H, n_W, n_C, f)
    Z_quantum = quantum_compute_convolution_cirq(X_pad_quantum, W, b, stride, n_H, n_W, n_C, f)
    match_convolution = np.allclose(Z_classical, Z_quantum, atol=1e-6)
    print("Compute Convolution Function Match:", match_convolution)
    if not match_convolution:
        print("Discrepancy in compute_convolution function.")

    # Test convolution_forward function
    Z_forward_classical = convolution_forward(X, W, b, stride, padding)
    Z_forward_quantum = quantum_convolution_forward_cirq(X, W, b, stride, padding)
    match_forward = np.allclose(Z_forward_classical, Z_forward_quantum, atol=1e-6)
    print("Convolution Forward Function Match:", match_forward)
    if not match_forward:
        print("Discrepancy in convolution_forward function.")

    # Test compute_grads function
    dX_classical, dW_classical, db_classical = compute_grads(dZ, X_pad_classical, W, stride, n_H, n_W, n_C, f, padding)
    dX_quantum, dW_quantum, db_quantum = quantum_compute_grads_cirq(dZ, X_pad_quantum, W, stride, n_H, n_W, n_C, f, padding)
    match_dX = np.allclose(dX_classical, dX_quantum, atol=1e-6)
    match_dW = np.allclose(dW_classical, dW_quantum, atol=1e-6)
    match_db = np.allclose(db_classical, db_quantum, atol=1e-6)
    print("Compute Gradients Function Match:", match_dX and match_dW and match_db)
    if not match_dX:
        print("Discrepancy in gradient w.r.t input dX.")
    if not match_dW:
        print("Discrepancy in gradient w.r.t weights dW.")
    if not match_db:
        print("Discrepancy in gradient w.r.t biases db.")

    # Test convolution_backward function
    dX_bwd_classical, dW_bwd_classical, db_bwd_classical = convolution_backward(dZ, X, W, stride, padding)
    dX_bwd_quantum, dW_bwd_quantum, db_bwd_quantum = quantum_convolution_backward_cirq(dZ, X, W, stride, padding)
    match_backward = (np.allclose(dX_bwd_classical, dX_bwd_quantum, atol=1e-6) and
                      np.allclose(dW_bwd_classical, dW_bwd_quantum, atol=1e-6) and
                      np.allclose(db_bwd_classical, db_bwd_quantum, atol=1e-6))
    print("Convolution Backward Function Match:", match_backward)
    if not match_backward:
        print("Discrepancy in convolution_backward function.")

# Example usage
if __name__ == "__main__":
    X = np.random.rand(3, 10, 10)
    W = np.random.rand(8, 3, 3, 3)
    b = np.random.rand(8)
    dZ = np.random.rand(8, 10, 10)
    stride = 1
    padding = 1
    test_convolution_pieces(X, W, b, dZ, stride, padding)
```