
import numpy as np
import cirq
from QuantumPoolGradientsCirq import quantum_pool_gradients_cirq

def quantum_pool_backward_cirq(dX_pool, X, f=2, stride=2, mode='max'):
    return quantum_pool_gradients_cirq(dX_pool, X, f, stride, mode)
