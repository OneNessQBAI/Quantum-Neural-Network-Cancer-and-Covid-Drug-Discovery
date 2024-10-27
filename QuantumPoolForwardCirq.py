
import numpy as np
import cirq
from QuantumPoolLayerCirq import quantum_pool_layer_cirq

def quantum_pool_forward_cirq(X, f=2, stride=2, mode='max'):
    return quantum_pool_layer_cirq(X, f, stride, mode)
