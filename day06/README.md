# Day 06: Structural Biology API Data Fetcher (RCSB PDB)

This project connects to the official **RCSB Protein Data Bank REST API** to programmatically fetch structural metadata for biological macromolecules.

## About the Database & Targeted Protein
The RCSB PDB is a global repository containing 3D structural data for macromolecules determined by experimental methods such as X-ray Crystallography, Cryo-EM, and **Nuclear Magnetic Resonance**. 

For this assignment, the script targets PDB entry **6Z5N**, which represents the structure of the **DNAJB1-JD** chaperone. What is it? It is a protein from the chaperone family – the cell’s “babysitters” who help other proteins fold correctly and prevent them from collapsing and forming dangerous clumps.

The main part (the J-Domain): At its tip there is a small, rigid region consisting of 4 helices (the J-domain). This region has a triplet of amino acids (HPD) that acts like a digital handshake – it binds to the larger chaperone (Hsp70) and activates it.

Why is it used in my lab? Since it is a stable, small and highly studied protein, its J-domain structure is used as a “classical model” in NMR to compare it to other J proteins to understand how small changes in structure affect the cell’s ability to fight drugs.

The tool programmatically extracts:
1. **Experimental Method:** Identifies how the structure was solved ( `SOLUTION NMR`).
2. **Resolution Metrics:** Determines the experimental resolution limits (which return as `None`/Not Applicable for standard NMR structural ensembles).

## Features
- Fetches real-time JSON metadata from the live RCSB PDB API endpoints using the Python `requests` library.
- Safely parses complex, deeply nested JSON responses using robust dictionary `.get()` mechanisms to prevent runtime exceptions.

## Interaction with AI
During this assignment, I used **Gemini (Google AI)** to assist with:
- Formatting the REST API URL endpoint for the RCSB PDB database.
- Writing the dictionary parsing logic to extract deep JSON values using `.get()`.
- Setting up the isolated `test_pdb.py` file with mock data.
- Troubleshooting local dependency installation issues in PowerShell.
