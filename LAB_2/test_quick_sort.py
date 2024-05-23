import unittest
from quick_sort import quick_sort

class TestQuick(unittest.TestCase):
        
    def test_quick_sort_empty(self):
        arr = []
        quick_sort(arr, 0 , len(arr)-1)
        self.assertListEqual(arr, [])
        
    def test_quick_sort(self):
        arr = [5, 2, 9, 1, 7]
        quick_sort(arr, 0 , len(arr)-1)
        self.assertListEqual(arr, [1, 2, 5, 7, 9])
        
if __name__ == "__main__":
    unittest.main()
    
    
    