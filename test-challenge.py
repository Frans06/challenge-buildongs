import unittest
import sys
sys.path.append("..")

from challenge import silhouette_extractor

class SilhouetteTestCase(unittest.TestCase):
    # Simple test case
    def test_input_simple(self):
        input = [[1, 3, 2], [2, 4, 1]]
        output = [[1, 2], [3, 1], [4, 0]]
        self.assertEqual(silhouette_extractor(input), output)
    
    # On document test case
    def test_document_input(self):
        input = [[2, 9, 10], [3, 6, 15], [5, 12, 12], [13, 16, 10], [15, 17, 5]]
        output = [[2, 10], [3, 15], [6, 12], [12, 0], [13, 10], [16, 5], [17, 0]]
        self.assertEqual(silhouette_extractor(input), output)

    # Test a straight silhouette on same height overlap buildings 
    def test_continious_height_input(self):
        input = [[1, 4, 6], [2, 5, 8], [3, 7, 8], [4, 6, 6]]
        output = [[1, 6], [2, 8], [7, 0]]
        self.assertEqual(silhouette_extractor(input), output)

if __name__ == '__main__':
    unittest.main()
