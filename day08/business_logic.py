import requests

def fetch_pdb_metadata(pdb_id: str):
    """מורידה נתונים גולמיים ממאגר ה-PDB בצורה בטוחה"""
    # ניקוי הקלט כדי למנוע הזרקות קוד או תווים זדוניים (סניטציה)
    clean_id = "".join(c for c in pdb_id if c.isalnum())[:4]
    
    if len(clean_id) != 4:
        return None
        
    url = f"https://data.rcsb.org/rest/v1/core/entry/{clean_id.lower()}"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return response.json()
    except requests.RequestException:
        return None
    return None

def extract_structural_info(data):
    """מחלצת את שיטת הניסוי והרזולוציה מתוך מבנה הנתונים"""
    if not data:
        return {"error": "No data available"}
    
    rcsb_info = data.get("rcsb_entry_info", {})
    methods = rcsb_info.get("experimental_method", ["Unknown"])
    primary_method = methods[0] if methods else "Unknown"
    
    resolution = rcsb_info.get("resolution_combined", [None])
    primary_resolution = resolution[0] if resolution else None
    
    return {
        "method": primary_method,
        "resolution": primary_resolution
    }