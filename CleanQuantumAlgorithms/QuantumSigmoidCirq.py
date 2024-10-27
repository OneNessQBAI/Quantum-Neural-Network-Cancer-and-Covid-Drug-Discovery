```python
import cirq
import numpy as np

def quantum_sigmoid_cirq(x):
    # Normalize x to [0, 1], assuming x in [-6, 6]
    x_min, x_max = -6, 6
    normalized_x = (x - x_min) / (x_max - x_min)

    # Map normalized_x to rotation angle between 0 and pi/2
    theta = normalized_x * (np.pi / 2)

    # Create a qubit and a circuit
    qubit = cirq.GridQubit(0, 0)
    circuit = cirq.Circuit()

    # Apply rotation around Y-axis based on input
    circuit.append(cirq.ry(2 * theta)(qubit))

    # Measure the qubit
    circuit.append(cirq.measure(qubit, key='result'))

    # Simulate the circuit
    simulator = cirq.Simulator()
    result = simulator.run(circuit, repetitions=8192)
    counts = result.histogram(key='result')

    # Calculate probability of measuring '1'
    prob_one = counts.get(1, 0) / 8192

    return prob_one
```