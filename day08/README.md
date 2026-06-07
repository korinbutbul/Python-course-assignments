# Day 08: Web Application Framework for DNP-HMQC-PeakAnalyzer

This folder implements a modern web service architecture for our structural biology pipeline (**DNP-HMQC-PeakAnalyzer**) using **FastAPI**.

## Separation of Business Logic and Application Security
- **Decoupled Business Logic:** Core algorithms filtering out spectral noise and categorizing structural cross-peaks based on biological shifts (`1H`/`13C` ppm boundaries) are entirely contained inside `business_logic.py`.
- **Bobby Tables & Input Attack Safeguards:** To ensure web security, endpoint routes in `app.py` process parameter fields dynamically using explicit scalar typing constraints (`float`). Furthermore, range validation validation guards intercept and discard non-physical chemical coordinates before they can reach back-end arrays.
- **AI-Generated Code Verification:** logic structures scaffolded via AI assistance were double-checked utilizing local, offline programmatic unit tests to guarantee structural reliability and avoid potential security hallucinations.

## Interaction with AI (Prompts Used)
1. *"How can I decouple a 2D NMR peak filtering and categorization algorithm into a modular business_logic file and wrap it with a FastAPI web controller?"*
2. *"What inputs constraints should be implemented in Python to secure an analytical biochemistry database web interface from malicious parameter injection attacks?"*
3. *"How do I write unified unit tests validating both chemical shift categorization rules and FastAPI route response states using TestClient?"*

## Project Layout
```text
day08/
├── business_logic.py     # Functional core parsing, sorting, and noise screening
├── app.py                # FastAPI routing paths and data validations
├── test_app.py           # Verification suite checking calculation logic and requests
├── requirements.txt      # Web platform framework configurations
└── README.md             # Security explanations, instruction guides, and prompts