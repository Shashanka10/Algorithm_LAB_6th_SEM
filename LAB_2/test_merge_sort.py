import unittest
from merge_sort import merge_sort

class TestMergeSort(unittest.TestCase):
        
    def test_merge_sort_empty(self):
        arr = []
        merge_sort(arr, 0, len(arr) - 1) 
        self.assertListEqual(arr, [])
        
    def test_merge_sort(self):
        arr = [4, 2, 7, 1, 5, 3]
        merge_sort(arr, 0, len(arr) - 1) 
        self.assertListEqual(arr, [1, 2, 5, 4, 3, 7])
        
if __name__ == "__main__":
    unittest.main()