from fastapi import FastAPI, HTTPException
from business_logic import fetch_pdb_metadata, extract_structural_info

app = FastAPI(title="PDB Protein Structural Analytics API")

@app.get("/")
def home():
    """דף הבית של האפליקציה"""
    return {
        "message": "Welcome to the Protein Structural Analytics Web App!",
        "usage": "Go to /protein/{pdb_id} to fetch structure details. Example: /protein/6z5n"
    }

@app.get("/protein/{pdb_id}")
def get_protein_info(pdb_id: str):
    """נתיב דינמי שמחזיר מידע על החלבון לפי המזהה שהמשתמש מקליד בדפדפן"""
    raw_data = fetch_pdb_metadata(pdb_id)
    if not raw_data:
        raise HTTPException(status_code=404, detail="Protein data not found or invalid PDB ID")
        
    info = extract_structural_info(raw_data)
    return {
        "pdb_id": pdb_id.upper(),
        "experimental_method": info["method"],
        "resolution": info["resolution"] if info["resolution"] else "N/A (e.g., SOLUTION NMR Ensemble)"
    }