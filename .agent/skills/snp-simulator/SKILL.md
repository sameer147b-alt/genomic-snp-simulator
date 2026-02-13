---
name: snp-simulator
description: Orchestrates the simulation and GenAI impact prediction of DNA mutations.
---

# SNP Simulator

This skill orchestrates the simulation and GenAI impact prediction of DNA mutations.

## Workflow

### Phase 1: The Mutator ✅

Generate a wild-type DNA sequence and introduce random Single Nucleotide Polymorphisms (SNPs).

**Script:** `scripts/mutator.py`

### Phase 2: The Oracle ✅

Use an LLM API to evaluate the biological impact of the SNPs (e.g., predicting missense or nonsense mutations).

**Script:** `scripts/oracle.py`

### Phase 3: The Analyst ✅

Compile the prediction data and generate a Streamlit visualization.

**Script:** `scripts/analyst.py`

**Run:** `streamlit run scripts/analyst.py`
