import unittest
from pdb_fetcher import extract_structural_info

class TestPDBFetcher(unittest.TestCase):
    
    def test_extract_info_6z5n_simulation(self):
        # סימולציה מיועדת עבור נתוני ה-NMR protein 6Z5N
        mock_data = {
            "rcsb_entry_info": {
                "experimental_method": ["SOLUTION NMR"],
                "resolution_combined": [None]
            }
        }
        result = extract_structural_info(mock_data)
        self.assertEqual(result["method"], "SOLUTION NMR")
        self.assertIsNone(result["resolution"])

    def test_extract_info_empty(self):
        result = extract_structural_info(None)
        self.assertIn("error", result)

if __name__ == "__main__":
    unittest.main()