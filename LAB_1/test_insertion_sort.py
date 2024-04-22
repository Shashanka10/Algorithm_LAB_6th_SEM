import unittest
from insertion_sort import insertion_sort

class TestInsertion(unittest.TestCase):
    
    def test_insertion_sort(self):
        arr = [12, 10, 6, 14, 9]
        insertion_sort(arr)
        self.assertListEqual(arr, [6,9,10,12,14])
        
if __name__ == "__main__":
    unittest.main()
        