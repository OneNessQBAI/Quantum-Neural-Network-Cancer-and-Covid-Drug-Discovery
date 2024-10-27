
import numpy as np

def quantum_apply_dropout_back_cirq(dout, mask, dropout_rate):
    # Quantum implementation of apply_dropout_back
    # Since the mask is already generated, we can apply it directly
    # Scale the gradient using the mask
    dX = dout * mask / (1 - dropout_rate)
    return dX
