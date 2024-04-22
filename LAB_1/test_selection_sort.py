import unittest
from selection_sort import selection_sort

class TestSelection(unittest.TestCase):
    
    def test_selection_sort(self):
        arr = [64, 25, 12, 22, 11]
        selection_sort(arr)
        self.assertListEqual(arr, [11,12,22,25,64])
        
if __name__ == "__main__":
    unittest.main()
        