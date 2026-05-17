import unittest
from dna_analyzer import calculate_gc_content

class TestDNAAnalyzer(unittest.TestCase):
    
    def test_gc_content_normal(self):
        # רצף של 4 אותיות, חצי מהן G ו-C
        self.assertAlmostEqual(calculate_gc_content("ATGC"), 50.0)
        
    def test_gc_content_all_gc(self):
        self.assertAlmostEqual(calculate_gc_content("GGCC"), 100.0)
        
    def test_gc_content_empty(self):
        self.assertEqual(calculate_gc_content(""), 0.0)

if __name__ == "__main__":
    unittest.main()