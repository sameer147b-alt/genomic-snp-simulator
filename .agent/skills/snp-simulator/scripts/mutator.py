import random
import json
import os

def generate_dna(length=100):
    """Generates a random DNA sequence of a given length."""
    return ''.join(random.choices('ACTG', k=length))

def introduce_snps(sequence, num_snps=5):
    """Introduces random SNP mutations into the DNA sequence."""
    seq_list = list(sequence)
    length = len(sequence)
    mutations = []
    
    # helper to get a different base
    bases = ['A', 'C', 'T', 'G']
    
    indices = random.sample(range(length), num_snps)
    
    for idx in indices:
        original_base = seq_list[idx]
        possible_bases = [b for b in bases if b != original_base]
        mutated_base = random.choice(possible_bases)
        
        seq_list[idx] = mutated_base
        
        mutations.append({
            "index": idx,
            "original": original_base,
            "mutated": mutated_base
        })
    
    return ''.join(seq_list), mutations

def main():
    # 1. Generate Wild-Type Sequence
    wild_type_seq = generate_dna(100)
    
    # 2. Introduce Mutations
    mutated_seq, mutations_list = introduce_snps(wild_type_seq, 5)
    
    # 3. Prepare data for export
    output_data = {
        "wild_type_sequence": wild_type_seq,
        "mutated_sequence": mutated_seq,
        "mutations": mutations_list
    }
    
    # 4. Save to mutations.json
    # Determine the directory of the script to save the file there
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(script_dir, "mutations.json")
    
    with open(output_path, "w") as f:
        json.dump(output_data, f, indent=4)
        
    print(f"Success! Mutations generated and saved to {output_path}")

if __name__ == "__main__":
    main()
