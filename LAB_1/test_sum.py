import unittest
from sum import sum

class TestSum(unittest.TestCase):
    
    def test_sum(self):
        input_data = [3, 4, 2]
        result = sum(input_data)
        self.assertEqual(result, 9)
        
        input_data = []
        result = sum(input_data)
        self.assertEqual(result,0)
        
if __name__ == "__main__":
    unittest.main()
        