```python
import numpy as np
from Pooling import pool_layer, pool_forward, pool_gradients, pool_backward
from QuantumPoolLayerCirq import quantum_pool_layer_cirq
from QuantumPoolForwardCirq import quantum_pool_forward_cirq
from QuantumPoolGradientsCirq import quantum_pool_gradients_cirq
from QuantumPoolBackwardCirq import quantum_pool_backward_cirq

def test_pooling_pieces(X, dX_pool, f=2, stride=2, mode='max'):
    # Test pool_layer function
    X_pool_classical = pool_layer(X, f, stride, mode)
    X_pool_quantum = quantum_pool_layer_cirq(X, f, stride, mode)
    match_pool_layer = np.allclose(X_pool_classical, X_pool_quantum, atol=1e-6)
    print('Pool Layer Function Match:', match_pool_layer)
    if not match_pool_layer:
        print('Discrepancy in pool_layer function.')

    # Test pool_forward function
    X_pool_forward_classical = pool_forward(X, f, stride, mode)
    X_pool_forward_quantum = quantum_pool_forward_cirq(X, f, stride, mode)
    match_pool_forward = np.allclose(X_pool_forward_classical, X_pool_forward_quantum, atol=1e-6)
    print('Pool Forward Function Match:', match_pool_forward)
    if not match_pool_forward:
        print('Discrepancy in pool_forward function.')

    # Test pool_gradients function
    dX_classical = pool_gradients(dX_pool, X, f, stride, mode)
    dX_quantum = quantum_pool_gradients_cirq(dX_pool, X, f, stride, mode)
    match_pool_gradients = np.allclose(dX_classical, dX_quantum, atol=1e-6)
    print('Pool Gradients Function Match:', match_pool_gradients)
    if not match_pool_gradients:
        print('Discrepancy in pool_gradients function.')

    # Test pool_backward function
    dX_backward_classical = pool_backward(dX_pool, X, f, stride, mode)
    dX_backward_quantum = quantum_pool_backward_cirq(dX_pool, X, f, stride, mode)
    match_pool_backward = np.allclose(dX_backward_classical, dX_backward_quantum, atol=1e-6)
    print('Pool Backward Function Match:', match_pool_backward)
    if not match_pool_backward:
        print('Discrepancy in pool_backward function.')

# Example usage
if __name__ == '__main__':
    X = np.random.rand(3, 10, 10)
    dX_pool = np.random.rand(3, 5, 5)
    test_pooling_pieces(X, dX_pool, f=2, stride=2, mode='max')
```