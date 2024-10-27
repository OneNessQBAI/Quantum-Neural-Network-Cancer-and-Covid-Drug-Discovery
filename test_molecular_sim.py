from quantum_algorithms.quantum_molecular_sim import QuantumMolecularSimulator
import numpy as np

def test_protein_drug_interaction():
    # Initialize simulator
    simulator = QuantumMolecularSimulator(num_qubits_per_atom=4)
    
    # Example protein binding site coordinates (simplified)
    protein_coords = [
        (0.0, 0.0, 0.0),  # Central amino acid
        (0.2, 0.1, 0.1),  # Binding pocket residue 1
        (-0.1, 0.2, 0.1), # Binding pocket residue 2
        (0.1, -0.1, 0.2)  # Binding pocket residue 3
    ]
    
    # Example drug molecule coordinates
    drug_coords = [
        (0.0, 0.0, 0.1),  # Core structure
        (0.1, 0.1, 0.0),  # Functional group 1
        (-0.1, 0.1, 0.0)  # Functional group 2
    ]
    
    print("1. Testing Molecular Interaction Simulation...")
    binding_energy = simulator.calculate_binding_energy(protein_coords, drug_coords)
    print(f"Binding Energy Results: {binding_energy}")
    print("\n" + "="*50 + "\n")
    
    print("2. Testing Binding Affinity Prediction...")
    affinity = simulator.predict_binding_affinity(protein_coords, drug_coords)
    print(f"Binding Affinity Results: {affinity}")
    print("\n" + "="*50 + "\n")
    
    print("3. Testing Drug Candidate Optimization...")
    optimization = simulator.optimize_drug_candidate(protein_coords, drug_coords)
    print(f"Initial coordinates: {drug_coords}")
    print(f"Optimized coordinates: {optimization['optimized_coordinates']}")
    print(f"Energy improvement: {optimization['convergence_score']*100:.2f}%")
    print("\n" + "="*50 + "\n")

if __name__ == "__main__":
    print("Starting Quantum Molecular Simulation Tests\n")
    print("="*50 + "\n")
    test_protein_drug_interaction()
