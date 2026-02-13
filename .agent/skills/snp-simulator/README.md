# 🧬 Genomic SNP Simulator

**An agentic bioinformatics pipeline that simulates DNA mutations, predicts their biological impact using Google Gemini, and visualizes results through an interactive 3D protein dashboard.**

[![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-FF4B4B?logo=streamlit)](https://streamlit.io/)
[![Google Gemini](https://img.shields.io/badge/Powered%20by-Gemini%202.5%20Flash-4285F4?logo=google)](https://ai.google.dev/)

---

## 🧠 What Makes This Different?

This isn't a keyword-matching script or a monolithic Jupyter notebook. It is a **multi-agent orchestrated pipeline** built within Google's **Antigravity** agentic coding framework — where each phase was independently planned, implemented, and verified by an AI agent.

### Key Technical Features

| Feature | Description |
|---|---|
| **Multi-Agent Orchestration** | Built with Google Antigravity — each phase (Mutator, Oracle, Analyst) was independently managed as a discrete agentic task with its own planning, execution, and verification cycle |
| **GenAI Reasoning (not keyword matching)** | Each SNP is individually prompted to Gemini 2.5 Flash, which applies deep training on protein biochemistry, codon tables, and molecular biology to deliver functional annotation — a task that traditionally requires complex bioinformatics toolchains |
| **3D Protein Visualization** | Interactive, spinning ribbon models rendered with `py3Dmol` and `stmol`, dynamically color-coded by AI-predicted mutation severity (nonsense → yellow, missense → purple) |
| **Antigravity Skill Architecture** | Structured as a composable, multi-phase skill with a `SKILL.md` manifest — not a flat script, but a reusable agentic capability |
| **Production-Ready Security** | API keys loaded from environment variables via `python-dotenv` — zero hardcoded secrets |

---

## 🏗️ Architecture

The pipeline is designed as a **3-phase agentic skill**, where each phase is an independent, composable module:

```
Phase 1: The Mutator          Phase 2: The Oracle           Phase 3: The Analyst
┌──────────────────┐      ┌──────────────────────┐      ┌──────────────────────┐
│  Generate DNA    │      │  Gemini 2.5 Flash    │      │  Streamlit Dashboard │
│  wild-type seq   │─────▶│  evaluates each SNP  │─────▶│  3D protein viewer   │
│  + random SNPs   │      │  for bio impact      │      │  + charts + export   │
└──────────────────┘      └──────────────────────┘      └──────────────────────┘
   mutator.py                  oracle.py                    analyst.py
   └─▶ mutations.json         └─▶ predictions.json         └─▶ Interactive UI
```

### Antigravity Skill Structure

```
snp-simulator/
├── SKILL.md                  # Skill manifest (name, description, workflow)
├── README.md                 # This file
├── requirements.txt          # Python dependencies
├── .gitignore                # Git exclusions
└── scripts/
    ├── mutator.py            # Phase 1 — DNA sequence generation & SNP injection
    ├── oracle.py             # Phase 2 — Gemini-powered functional annotation
    ├── analyst.py            # Phase 3 — Streamlit dashboard with 3D viewer
    ├── mutations.json        # Phase 1 output (generated at runtime)
    └── predictions.json      # Phase 2 output (generated at runtime, gitignored)
```

---

## 🤖 Multi-Agent Orchestration

This project was not built as a single top-to-bottom script. It was developed using **Google Antigravity**, an agentic AI coding assistant that autonomously **planned, coded, tested, and debugged** each phase as an independent task:

| Phase | Agent Role | What Antigravity Did |
|---|---|---|
| **The Mutator** | Data Generator | Designed the random SNP injection algorithm, chose sequence length, wrote `mutations.json` schema |
| **The Oracle** | LLM Integrator | Selected Gemini 2.5 Flash, crafted the biomedical prompt, handled rate-limiting (429 errors), migrated from the deprecated `google-generativeai` to the new `google-genai` SDK |
| **The Analyst** | Dashboard Builder | Built the Streamlit app, integrated `py3Dmol` for 3D rendering, implemented mutation-aware color logic, added CSV export |
| **Deployment** | DevOps | Secured API keys, generated `requirements.txt`, authored `.gitignore`, drafted this README |

Each phase was independently orchestrated with its own **planning → execution → verification** cycle, making this a true demonstration of agentic software development.

---

## 🚀 Quick Start

### 1. Clone & Install

```bash
git clone https://github.com/sameer147b-alt/genomic-snp-simulator.git
cd genomic-snp-simulator
pip install -r requirements.txt
```

### 2. Set Your API Key

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_google_gemini_api_key_here
```

> Get a free API key at [aistudio.google.com](https://aistudio.google.com/)

### 3. Run the Pipeline

```bash
# Phase 1 — Generate mutations
python scripts/mutator.py

# Phase 2 — Get AI predictions
python scripts/oracle.py

# Phase 3 — Launch the dashboard
streamlit run scripts/analyst.py
```

---

## 📊 Dashboard Features

- **DNA Sequence Comparison** — Wild-type vs. mutated sequence side-by-side
- **3D Protein Viewer** — Spinning ribbon model (PDB: 1A2P) colored by mutation impact:
  - 🟡 **Yellow** — Nonsense mutation detected (truncated protein)
  - 🟣 **Purple** — Missense mutation detected (altered protein)
  - 🔵 **Cyan** — Synonymous mutations (structure unchanged)
- **Mutation Distribution Chart** — Bar chart of missense / nonsense / synonymous counts
- **Raw Data Table** — Full mutation index, bases, and AI predictions
- **CSV Export** — One-click download of all predictions

---

## 🔧 Tech Stack

| Component | Technology |
|---|---|
| DNA simulation | Python `random` module |
| LLM inference | Google Gemini 2.5 Flash via `google-genai` SDK |
| Dashboard | Streamlit |
| 3D rendering | py3Dmol + stmol |
| Data handling | Pandas |
| Secret management | python-dotenv |

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

<p align="center">
  Built with 🧬 by <a href="https://github.com/sameer147b-alt">sameer147b-alt</a>
</p>
