from quantum_algorithms.quantum_optimization import QuantumOptimization
from quantum_algorithms.quantum_grover import GroverOptimizer

def test_quantum_search():
    print("Testing Quantum Search Optimization...")
    optimizer = QuantumOptimization()
    
    # Test data
    test_data = [1, 3, 5, 7, 9, 11, 13, 15]
    target = 7
    
    print(f"Searching for {target} in dataset: {test_data}")
    result = optimizer.optimize(test_data)
    print("Search Result:", result)
    print("\n" + "="*50 + "\n")

def test_quantum_math():
    print("Testing Quantum Mathematical Optimization...")
    optimizer = QuantumOptimization()
    
    # Test value
    test_value = 42
    
    print(f"Optimizing value: {test_value}")
    result = optimizer.optimize(test_value)
    print("Math Optimization Result:", result)
    print("\n" + "="*50 + "\n")

def test_code_optimization():
    print("Testing Quantum Code Optimization...")
    optimizer = QuantumOptimization()
    
    # Test code
    test_code = """
def search_algorithm(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return i
    return -1
    """
    
    print("Original code:")
    print(test_code)
    print("\nOptimized code:")
    result = optimizer.optimize(test_code)
    print(result)

if __name__ == "__main__":
    print("Starting Quantum Algorithm Tests\n")
    print("="*50 + "\n")
    
    test_quantum_search()
    test_quantum_math()
    test_code_optimization()
