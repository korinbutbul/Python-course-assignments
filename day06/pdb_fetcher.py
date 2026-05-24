import requests

def fetch_pdb_metadata(pdb_id):
    """מוריד נתוני חלבון בפורמט JSON מתוך ה-API הרשמי של RCSB PDB"""
    url = f"https://data.rcsb.org/rest/v1/core/entry/{pdb_id.lower()}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None

def extract_structural_info(data):
    """מחלץ את שיטת הניסוי המבני ואת הרזולוציה מתוך ה-JSON"""
    if not data:
        return {"error": "No data available"}
    
    # חילוץ שיטות הניסוי (למשל SOLUTION NMR)
    methods = data.get("rcsb_entry_info", {}).get("experimental_method", ["Unknown"])
    primary_method = methods[0] if methods else "Unknown"
    
    # חילוץ רזולוציה
    resolution = data.get("rcsb_entry_info", {}).get("resolution_combined", [None])
    primary_resolution = resolution[0] if resolution else None
    
    return {
        "method": primary_method,
        "resolution": primary_resolution
    }

def main():
    # החלבן שאני חוקרת במעבדה
    pdb_id = "6Z5N" 
    print(f"Fetching data for PDB ID: {pdb_id}...")
    
    raw_data = fetch_pdb_metadata(pdb_id)
    if raw_data:
        info = extract_structural_info(raw_data)
        print(f"\n--- Structural Analysis Results for {pdb_id} ---")
        print(f"Experimental Method: {info['method']}")
        if info['resolution']:
            print(f"Resolution: {info['resolution']} Å")
        else:
            print("Resolution: N/A (Standard for SOLUTION NMR ensembles)")
    else:
        print("Failed to retrieve data. Please check the PDB ID or internet connection.")

if __name__ == "__main__":
    main()