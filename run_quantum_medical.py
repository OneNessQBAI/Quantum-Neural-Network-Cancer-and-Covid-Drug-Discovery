from quantum_medical_system import QuantumMedicalSystem
from system_prompts.quantum_medical_prompt import QuantumMedicalPrompt
import json

def main():
    print("Initializing Quantum Medical System...")
    system = QuantumMedicalSystem()
    prompt_generator = QuantumMedicalPrompt()

    # Configure drug discovery parameters for cancer research
    drug_params = {
        "disease": "Lung Cancer",
        "targets": ["EGFR", "ALK", "ROS1"],
        "mol_weight": "<500",
        "solubility": "High",
        "binding_affinity": "High"
    }

    # Generate task-specific prompt
    print("\nGenerating quantum-enhanced drug discovery prompt...")
    drug_prompt = prompt_generator.generate_task_prompt("drug_discovery", drug_params)

    # Example SMILES for potential cancer drugs
    test_compounds = [
        # EGFR inhibitor-like structures
        "CC1=C(C=C(C=C1)NC(=O)C2=CC=C(C=C2)CN3CCN(CC3)C)NC4=NC=CC(=N4)C5=CN=CC=C5",
        # ALK inhibitor-like structures
        "COC1=CC2=C(C=C1)C(=CN2)C3=CC=C(C=C3)C(=O)NC4=CC=C(C=C4)CN5CCN(CC5)C",
        # ROS1 inhibitor-like structures
        "CC1=CC(=CC=C1)NC2=NC=CC(=N2)C3=CN=CC=C3"
    ]

    print("\nPerforming quantum-entangled drug analysis...")
    results = system.quantum_entangled_analysis(test_compounds, "EGFR")

    print("\nAnalyzing results across quantum-connected medical databases...")
    for i, result in enumerate(results, 1):
        print(f"\nDrug Candidate {i}:")
        print(f"Binding Score: {result.binding_score:.2f}")
        print(f"Clinical Relevance: {result.clinical_relevance:.2f}")
        print("\nQuantum Properties:")
        for key, value in result.quantum_properties.items():
            print(f"{key}: {value}")

    # Search medical databases using quantum acceleration
    print("\nPerforming quantum-accelerated database search...")
    chembl_results = system.quantum_database_search("kinase inhibitor", "chembl")
    print(f"\nFound {len(chembl_results)} potential compounds in ChEMBL database")

    # Display top results
    print("\nTop Quantum-Analyzed Drug Candidates:")
    for i, result in enumerate(chembl_results[:3], 1):
        print(f"\nCandidate {i}:")
        print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
