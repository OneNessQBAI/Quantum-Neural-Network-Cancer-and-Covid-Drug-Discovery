from quantum_medical_system import QuantumMedicalSystem
from medical_applications.covid_spike_protein import CovidSpikeProteinAnalyzer
from medical_applications.cancer_drug_discovery import CancerDrugDesigner
from medical_applications.alzheimer_protein_analysis import AlzheimerProteinAnalyzer
from system_prompts.quantum_medical_prompt import QuantumMedicalPrompt
import json

def test_covid_analysis():
    print("\n=== COVID-19 Spike Protein Analysis ===")
    covid_analyzer = CovidSpikeProteinAnalyzer()
    
    # Template inhibitor structure
    template_inhibitor = [
        (0.0, 0.0, 0.1),   # Core scaffold
        (0.2, 0.1, 0.0),   # Binding group 1
        (-0.1, 0.2, 0.0),  # Binding group 2
        (0.1, -0.1, 0.2),  # Functional group 1
        (-0.2, -0.1, 0.1)  # Functional group 2
    ]
    
    print("Designing spike protein inhibitor...")
    results = covid_analyzer.design_spike_protein_inhibitor(template_inhibitor)
    
    print(f"Binding Energy: {results['optimized_binding_energy']:.2f}")
    print(f"Binding Affinity: {results['binding_affinity']:.2f}")
    print("Key Residue Interactions:")
    for residue, energy in results['key_residue_interactions'].items():
        print(f"{residue}: {energy:.2f}")

def test_cancer_drug_design():
    print("\n=== Cancer Drug Discovery Analysis ===")
    cancer_designer = CancerDrugDesigner()
    
    template_inhibitor = [
        (0.0, 0.0, 0.1),   # Core scaffold
        (0.2, 0.1, 0.0),   # Hinge-binding region
        (-0.1, 0.2, 0.0),  # Solvent-exposed region
        (0.1, -0.1, 0.2),  # T790M targeting group
        (-0.2, -0.1, 0.1)  # Selectivity element
    ]
    
    print("Designing selective EGFR inhibitor...")
    results = cancer_designer.design_selective_inhibitor(template_inhibitor)
    
    print(f"Mutant Binding Energy: {results['mutant_binding_energy']:.2f}")
    print(f"Wild-type Binding Energy: {results['wildtype_binding_energy']:.2f}")
    print(f"Selectivity Ratio: {results['selectivity_ratio']:.2f}")
    print(f"Predicted Efficacy: {results['predicted_efficacy']['mutant_inhibition']*100:.1f}%")

def test_alzheimer_analysis():
    print("\n=== Alzheimer's Disease Analysis ===")
    alzheimer_analyzer = AlzheimerProteinAnalyzer()
    
    print("Simulating protein misfolding...")
    misfolding_results = alzheimer_analyzer.simulate_protein_misfolding(
        alzheimer_analyzer.abeta_monomer_coords,
        time_steps=5
    )
    
    print(f"Energy Change: {misfolding_results['misfolding_metrics']['energy_change']:.2f}")
    print(f"Structural Change: {misfolding_results['misfolding_metrics']['structural_change']:.2f}")
    
    print("\nAnalyzing aggregation propensity...")
    aggregation_results = alzheimer_analyzer.analyze_aggregation_propensity(
        alzheimer_analyzer.tau_monomer_coords,
        {'temperature': 1.0, 'energy_threshold': -0.5}
    )
    
    print(f"Aggregation Probability: {aggregation_results['aggregation_probability']:.2f}")
    print(f"Mean Interaction Energy: {aggregation_results['mean_interaction_energy']:.2f}")

def test_quantum_database_integration():
    print("\n=== Quantum Database Integration ===")
    system = QuantumMedicalSystem()
    prompt_gen = QuantumMedicalPrompt()
    
    # Configure search parameters
    drug_params = {
        "disease": "Cancer",
        "targets": ["EGFR", "ALK"],
        "mol_weight": "<500"
    }
    
    print("Performing quantum-accelerated database search...")
    results = system.quantum_database_search("kinase inhibitor", "chembl")
    
    print(f"\nFound {len(results)} potential compounds")
    print("\nTop candidates:")
    for i, result in enumerate(results[:3], 1):
        print(f"\nCandidate {i}:")
        print(json.dumps(result, indent=2))

def main():
    print("Starting Unified Quantum Medical System Tests")
    print("=" * 50)
    
    try:
        test_covid_analysis()
    except Exception as e:
        print(f"COVID analysis error: {e}")
    
    try:
        test_cancer_drug_design()
    except Exception as e:
        print(f"Cancer drug design error: {e}")
    
    try:
        test_alzheimer_analysis()
    except Exception as e:
        print(f"Alzheimer analysis error: {e}")
    
    try:
        test_quantum_database_integration()
    except Exception as e:
        print(f"Database integration error: {e}")
    
    print("\nQuantum Medical System Tests Complete")
    print("=" * 50)

if __name__ == "__main__":
    main()
