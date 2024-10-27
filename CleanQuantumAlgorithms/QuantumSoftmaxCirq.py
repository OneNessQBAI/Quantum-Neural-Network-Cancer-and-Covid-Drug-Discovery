```python
import numpy as np
from QuantumExponentiationCirq import quantum_exponentiation_cirq
from QuantumSummationCirq import quantum_summation_cirq
from QuantumDivisionCirq import quantum_division_cirq

def quantum_softmax_cirq(x):
    exp_x = quantum_exponentiation_cirq(x)
    sum_exp_x = quantum_summation_cirq(exp_x)
    softmax_output = quantum_division_cirq(exp_x, sum_exp_x)
    return softmax_output
```