```python
import numpy as np
from Dropout import apply_dropout, apply_dropout_back
from QuantumApplyDropoutCirq import quantum_apply_dropout_cirq
from QuantumApplyDropoutBackCirq import quantum_apply_dropout_back_cirq

def test_dropout_pieces(X, dropout_rate):
    # Classical computations
    out_classical, mask_classical = apply_dropout(X, dropout_rate)
    dout = np.random.rand(*out_classical.shape)
    dX_classical = apply_dropout_back(dout, mask_classical, dropout_rate)

    # Quantum computations
    out_quantum, mask_quantum = quantum_apply_dropout_cirq(X, dropout_rate)
    dX_quantum = quantum_apply_dropout_back_cirq(dout, mask_quantum, dropout_rate)

    # Compare outputs
    match_forward = np.allclose(out_classical, out_quantum, atol=1e-6)
    print('Apply Dropout Function Match:', match_forward)
    if not match_forward:
        print('Discrepancy in apply_dropout function.')

    # Compare masks
    match_mask = np.array_equal(mask_classical, mask_quantum)
    print('Dropout Mask Match:', match_mask)
    if not match_mask:
        print('Discrepancy in dropout mask.')

    # Compare backward pass
    match_backward = np.allclose(dX_classical, dX_quantum, atol=1e-6)
    print('Apply Dropout Backward Function Match:', match_backward)
    if not match_backward:
        print('Discrepancy in apply_dropout_back function.')

# Example usage
if __name__ == '__main__':
    X = np.random.rand(3, 5)
    dropout_rate = 0.5
    test_dropout_pieces(X, dropout_rate)
```