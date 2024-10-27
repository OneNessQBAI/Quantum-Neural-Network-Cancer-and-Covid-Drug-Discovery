from quantum_medical_system import QuantumMedicalSystem
from medical_applications.covid_spike_protein import CovidSpikeProteinAnalyzer
from medical_applications.cancer_drug_discovery import CancerDrugDesigner
from medical_applications.alzheimer_protein_analysis import AlzheimerProteinAnalyzer
import numpy as np
import json

def print_section(title):
    print(f"\n{'='*20} {title} {'='*20}\n")

def test_integrated_drug_discovery():
    print_section("Integrated Drug Discovery")
    
    system = QuantumMedicalSystem()
    cancer_designer = CancerDrugDesigner()
    
    # Search for compounds
    print("1. Quantum Database Search")
    compounds = system.quantum_database_search("kinase inhibitor", "chembl")
    print(f"Found {len(compounds)} potential compounds")
    
    # Select test compounds
    test_smiles = [compound["smiles"] for compound in compounds]
    
    # Analyze with quantum entanglement
    print("\n2. Quantum-Entangled Analysis")
    results = system.quantum_entangled_analysis(test_smiles, "EGFR")
    
    print("\n3. Top Drug Candidates:")
    for i, result in enumerate(results, 1):
        print(f"\nCandidate {i}:")
        print(f"Binding Score: {result.binding_score:.2f}")
        print(f"Clinical Relevance: {result.clinical_relevance:.2f}")
        
        # Additional quantum properties
        if result.quantum_properties:
            print("\nQuantum Properties:")
            for key, value in result.quantum_properties.items():
                if isinstance(value, float):
                    print(f"{key}: {value:.3f}")
                else:
                    print(f"{key}: {value}")

def test_covid_analysis():
    print_section("COVID-19 Spike Protein Analysis")
    
    analyzer = CovidSpikeProteinAnalyzer()
    
    # Test coordinates for potential inhibitor
    template_coords = [
        (0.0, 0.0, 0.1),   # Core scaffold
        (0.2, 0.1, 0.0),   # Binding group 1
        (-0.1, 0.2, 0.0),  # Binding group 2
        (0.1, -0.1, 0.2),  # Functional group 1
        (-0.2, -0.1, 0.1)  # Functional group 2
    ]
    
    print("1. Designing Spike Protein Inhibitor")
    results = analyzer.design_spike_protein_inhibitor(template_coords)
    
    print("\n2. Analysis Results:")
    print(f"Binding Energy: {results['optimized_binding_energy']:.2f}")
    print(f"Improvement: {results['improvement_percentage']:.1f}%")
    
    print("\n3. Key Residue Interactions:")
    for residue, energy in results['key_residue_interactions'].items():
        print(f"{residue}: {energy:.2f}")

def test_alzheimer_analysis():
    print_section("Alzheimer's Disease Analysis")
    
    analyzer = AlzheimerProteinAnalyzer()
    
    print("1. Protein Misfolding Simulation")
    misfolding_results = analyzer.simulate_protein_misfolding(
        analyzer.abeta_monomer_coords,
        time_steps=5
    )
    
    print("\n2. Misfolding Results:")
    print(f"Energy Change: {misfolding_results['misfolding_metrics']['energy_change']:.2f}")
    print(f"Structural Change: {misfolding_results['misfolding_metrics']['structural_change']:.2f}")
    
    print("\n3. Aggregation Analysis")
    aggregation_results = analyzer.analyze_aggregation_propensity(
        analyzer.tau_monomer_coords,
        {'temperature': 1.0, 'energy_threshold': -0.5}
    )
    
    print("\n4. Aggregation Results:")
    print(f"Aggregation Probability: {aggregation_results['aggregation_probability']:.2f}")
    print(f"Mean Interaction Energy: {aggregation_results['mean_interaction_energy']:.2f}")

def test_cross_application_analysis():
    print_section("Cross-Application Quantum Analysis")
    
    system = QuantumMedicalSystem()
    
    # Test unified quantum properties
    test_coords = [
        (0.0, 0.0, 0.0),
        (0.2, 0.1, 0.1),
        (-0.1, 0.2, 0.1)
    ]
    
    print("1. Quantum Property Analysis")
    binding_result = system.quantum_sim.calculate_binding_energy(test_coords, test_coords)
    print(f"\nBinding Energy: {binding_result['binding_energy']:.2f}")
    print(f"Confidence Score: {binding_result['confidence_score']:.2f}")
    
    print("\n2. Electron Density Analysis")
    circuit = system.quantum_sim.create_molecular_encoding_circuit(test_coords)
    density = system.quantum_sim.simulate_electron_density(circuit, len(test_coords))
    print(f"Mean Electron Density: {np.mean(density):.3f}")

def main():
    print("\nStarting Unified Quantum Medical Analysis")
    print("="*60)
    
    try:
        test_integrated_drug_discovery()
    except Exception as e:
        print(f"Error in drug discovery: {e}")
    
    try:
        test_covid_analysis()
    except Exception as e:
        print(f"Error in COVID analysis: {e}")
    
    try:
        test_alzheimer_analysis()
    except Exception as e:
        print(f"Error in Alzheimer analysis: {e}")
    
    try:
        test_cross_application_analysis()
    except Exception as e:
        print(f"Error in cross-application analysis: {e}")
    
    print("\nQuantum Medical Analysis Complete")
    print("="*60)

if __name__ == "__main__":
    main()
