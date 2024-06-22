#convert a number to its binary representation as a string
import unittest

def convert_to_binary(num, length):
    return format(num, f'0{length}b')

def bruteforce_01_knapSack(p, w, m):

    assert len(p) == len(w), "p and w differ in length"
    
    n = len(p)
    max_profit = 0
    total_capacity = m
    solution = ""

    # Generate all possible combinations of items
    for i in range(2**n):
        # Convert binary representation to string
        s = convert_to_binary(i, n)
        
        # Compute total profit and weight for current combination
        profit = 0
        weight = 0
        for j in range(n):
            if s[j] == '1':
                profit += p[j]
                weight += w[j]
        
        # Check if current combination is feasible and more profitable than previous ones
        if weight <= total_capacity and profit > max_profit:
            max_profit = profit
            solution = s

    # Return maximum profit and solution string
    return max_profit, solution

#Example
profits = [60, 100, 120]
weights = [10, 20, 30]
max_capacity = 30

max_profit, solution = bruteforce_01_knapSack(profits, weights, max_capacity)
print("The feasible solution is:", solution)
print("Maximum Profit is:", max_profit)

class TestKnapsack(unittest.TestCase):
    def test_bruteforce_01_knapsack(self):
        expected_max_profit = 160
        expected_solution = "110"
        
        max_profit, solution = bruteforce_01_knapSack(profits, weights, max_capacity)
        self.assertEqual(max_profit, expected_max_profit)
        self.assertEqual(solution, expected_solution)

if __name__ == "__main__":
    unittest.main()

