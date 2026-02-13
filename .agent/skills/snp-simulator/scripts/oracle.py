from google import genai
from dotenv import load_dotenv
import json
import os
import time

# Load environment variables from .env file (if present)
load_dotenv()

# Initialize the client with the API key from environment
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise EnvironmentError(
        "GEMINI_API_KEY not found. "
        "Set it in a .env file or export it as an environment variable."
    )
client = genai.Client(api_key=api_key)

def main():
    # Determine file paths
    script_dir = os.path.dirname(os.path.abspath(__file__))
    mutations_path = os.path.join(script_dir, "mutations.json")
    predictions_path = os.path.join(script_dir, "predictions.json")

    # Read mutations.json
    try:
        with open(mutations_path, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Error: {mutations_path} not found. Please run mutator.py first.")
        return

    mutations = data.get("mutations", [])
    wild_type_seq = data.get("wild_type_sequence", "")
    mutated_seq = data.get("mutated_sequence", "")
    
    predictions_list = []
    
    print(f"Processing {len(mutations)} mutations with The Oracle...")

    # Loop through each mutation
    for mut in mutations:
        original_base = mut.get("original")
        mutated_base = mut.get("mutated")
        
        # Construct the prompt
        prompt = (f"I have a DNA mutation in a protein-coding region. "
                  f"The wild-type base is {original_base} and the mutated base is {mutated_base}. "
                  f"Predict the most likely biological impact of this Single Nucleotide Polymorphism (SNP). "
                  f"Is it likely synonymous, missense, or nonsense? Keep your answer to one short sentence.")
        
        try:
            # Send prompt to the model
            response = client.models.generate_content(model='gemini-2.5-flash', contents=prompt)
            prediction_text = response.text.strip()
        except Exception as e:
            prediction_text = f"Error: {str(e)}"
            
        # Add prediction to the mutation data
        mutation_with_prediction = mut.copy()
        mutation_with_prediction["prediction"] = prediction_text
        predictions_list.append(mutation_with_prediction)
        
        # Be polite to the API
        time.sleep(4)

    # Prepare final data
    output_data = {
        "wild_type_sequence": wild_type_seq,
        "mutated_sequence": mutated_seq,
        "predictions": predictions_list
    }

    # Save to predictions.json
    with open(predictions_path, "w") as f:
        json.dump(output_data, f, indent=4)

    print(f"Success! Predictions generated and saved to {predictions_path}")

if __name__ == "__main__":
    main()
