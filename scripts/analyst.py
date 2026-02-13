import streamlit as st
import json
import pandas as pd
import os
from stmol import showmol
import py3Dmol

def get_dominant_mutation_type(predictions):
    """Determine the dominant mutation type from predictions."""
    counts = {"missense": 0, "nonsense": 0, "synonymous": 0}
    for pred in predictions:
        prediction_text = pred.get("prediction", "").lower()
        if "missense" in prediction_text:
            counts["missense"] += 1
        if "nonsense" in prediction_text:
            counts["nonsense"] += 1
        if "synonymous" in prediction_text:
            counts["synonymous"] += 1
    return counts

def render_protein_3d(mutation_counts):
    """Render a 3D protein model colored by dominant mutation type."""
    # Determine color based on mutation predictions
    if mutation_counts["nonsense"] > 0:
        ribbon_color = "yellow"  # Bright Yellow = truncated protein
        label = "⚠️ Nonsense mutation detected — showing truncated protein (Yellow)"
    elif mutation_counts["missense"] > 0:
        ribbon_color = "purple"  # Purple = missense / altered protein
        label = "🔬 Missense mutation detected — showing altered protein (Purple)"
    else:
        ribbon_color = "cyan"  # Default for synonymous
        label = "✅ Synonymous mutations — protein structure unchanged (Cyan)"

    st.info(label)

    # Create the 3D viewer with PDB 1A2P
    viewer = py3Dmol.view(query="pdb:1A2P", width=700, height=500)
    viewer.setStyle({"cartoon": {"color": ribbon_color}})
    viewer.setBackgroundColor("#0e1117")
    viewer.spin(True)
    viewer.zoomTo()

    showmol(viewer, height=500, width=700)

def main():
    st.set_page_config(page_title="Genomic SNP Simulator", page_icon="🧬", layout="wide")
    st.title("🧬 Genomic SNP Simulator Dashboard")

    # Determine file paths — always relative to this script's location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    predictions_path = os.path.join(script_dir, "predictions.json")

    # Read predictions.json
    try:
        with open(predictions_path, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        st.error(f"Error: predictions.json not found. Please run mutator.py and oracle.py first.")
        return

    wild_type_seq = data.get("wild_type_sequence", "")
    mutated_seq = data.get("mutated_sequence", "")
    predictions = data.get("predictions", [])

    # Display sequences
    st.subheader("Wild-Type Sequence")
    st.code(wild_type_seq, language="text")

    st.subheader("Mutated Sequence")
    st.code(mutated_seq, language="text")

    # --- 3D Protein Structural Prediction ---
    st.markdown("---")
    st.subheader("3D Protein Structural Prediction")
    st.caption("Placeholder structure (PDB: 1A2P) colored by predicted mutation impact.")

    counts = get_dominant_mutation_type(predictions)
    render_protein_3d(counts)

    # --- Mutation Type Distribution ---
    st.markdown("---")
    st.subheader("Mutation Type Distribution")
    chart_data = pd.DataFrame({
        "Mutation Type": list(counts.keys()),
        "Count": list(counts.values())
    }).set_index("Mutation Type")
    st.bar_chart(chart_data)

    # --- Raw Data Table ---
    st.subheader("Raw Mutation Data & AI Predictions")
    df = pd.DataFrame(predictions)
    st.dataframe(df, use_container_width=True)

    # --- CSV Download ---
    st.markdown("---")
    csv_data = df.to_csv(index=False)
    st.download_button(
        label="📥 Download Predictions as CSV",
        data=csv_data,
        file_name="snp_predictions.csv",
        mime="text/csv"
    )

if __name__ == "__main__":
    main()
