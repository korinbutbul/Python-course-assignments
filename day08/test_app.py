import unittest
from fastapi.testclient import TestClient
from app import app
from business_logic import extract_structural_info

class TestProteinWebApp(unittest.TestCase):
    
    def setUp(self):
        # יצירת קליינט בדיקה ייעודי לאפליקציית הרשת
        self.client = TestClient(app)

    def test_business_logic_parsing(self):
        """בדיקת הלוגיקה המדעית הטהורה"""
        mock_data = {
            "rcsb_entry_info": {
                "experimental_method": ["SOLUTION NMR"],
                "resolution_combined": [None]
            }
        }
        result = extract_structural_info(mock_data)
        self.assertEqual(result["method"], "SOLUTION NMR")
        self.assertIsNone(result["resolution"])

    def test_web_app_home_endpoint(self):
        """בדיקה שדף הבית של האפליקציה עולה בהצלחה"""
        response = self.client.get("/")
        self.assertEqual(response.status_code == 200, True)
        self.assertIn("Welcome", response.json()["message"])

    def test_web_app_invalid_protein(self):
        """בדיקה שהמערכת מגיבה בצורה בטוחה ונכונה לקלט שגוי"""
        response = self.client.get("/protein/INVALID_ID")
        self.assertEqual(response.status_code == 404, True)

if __name__ == "__main__":
    unittest.main()