---
name: snp-simulator
description: Orchestrates the simulation and GenAI impact prediction of DNA mutations.
---

# SNP Simulator

This skill orchestrates the simulation and GenAI impact prediction of DNA mutations using a multi-agent pipeline managed by Google Antigravity.

## Workflow

### Phase 1: The Mutator ✅

Generate a wild-type DNA sequence and introduce random Single Nucleotide Polymorphisms (SNPs).

**Script:** `scripts/mutator.py`
**Output:** `scripts/mutations.json`

### Phase 2: The Oracle ✅

Use Google Gemini 2.5 Flash to evaluate the biological impact of each SNP via agentic reasoning (functional annotation, not keyword matching).

**Script:** `scripts/oracle.py`
**Output:** `scripts/predictions.json`

### Phase 3: The Analyst ✅

Compile the prediction data and generate a Streamlit dashboard with interactive 3D protein visualization.

**Script:** `scripts/analyst.py`
**Run:** `streamlit run scripts/analyst.py`

### Phase 4: Deployment ✅

- Secured API keys via environment variables (`python-dotenv`)
- Generated `requirements.txt` with all dependencies
- Created `.gitignore` for clean repository
- Authored professional `README.md`
- Published to GitHub

**Status:** 🟢 **Live** — All phases complete and deployment-ready.
