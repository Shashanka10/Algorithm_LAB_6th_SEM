import unittest

class Item:
    def __init__(self, profit, weight):
        self.profit = profit
        self.weight = weight

def brute_force_fractional_knapsack(profits, weights, capacity):
    assert len(profits) == len(weights), "Length of profits and weights must be the same"
    
    n = len(profits)
    items = []
    
    # Create list of Item objects
    for i in range(n):
        items.append(Item(profits[i], weights[i]))
    
    # Sort items based on profit in decreasing order
    items.sort(key=lambda x: x.profit, reverse=True)
    
    total_profit = 0
    
    for item in items:
        current_weight = 0
        current_profit = 0
        current_solution = []
        
        for item in items:
            if current_weight + item.weight <= capacity:
                current_weight += item.weight
                current_profit += item.profit
                current_solution.append((item.profit, item.weight, 1))  # 1 means the full item is taken
            else:
                remaining_capacity = capacity - current_weight
                fraction = remaining_capacity / item.weight
                current_profit += item.profit * fraction
                current_weight += item.weight * fraction
                current_solution.append((item.profit, item.weight, fraction))  # fraction taken
                break  # Knapsack is full
        
        # Update maximum profit and best solution if current subset yields higher profit
        if current_profit > total_profit:
            total_profit = current_profit
            best_subset = current_solution
    
    return total_profit, best_subset

# Example usage:
profits = [10, 15, 7, 8, 9, 4]
weights = [3, 5, 4, 1, 3, 2]
max_capacity = 15

total_profit, solution = brute_force_fractional_knapsack(profits, weights, max_capacity)
print("Maximum Profit is:", total_profit)
print("The feasible solution are:")
for profit, weight, fraction in solution:
    print(f"Item with profit {profit} and weight {weight} is taken with fraction {fraction}")

# Test case for brute-force fractional knapsack
class TestKnapsack(unittest.TestCase):
    def test_bruteforce_fractional_knapsack(self):
        
        expected_total_profit = 47.25  # 15 + 10 + 9 + 8 + 5.25 (7 * 0.75)
        expected_solution = [
            (15, 5, 1),  # Full item with profit 15 and weight 5
            (10, 3, 1),  # Full item with profit 10 and weight 3
            (9, 3, 1),   # Full item with profit 9 and weight 3
            (8, 1, 1),   # Full item with profit 8 and weight 1
            (7, 4, 0.75) # 0.75 fraction of item with profit 7 and weight 4
        ]
        total_profit, solution = brute_force_fractional_knapsack(profits, weights, max_capacity)
        
        self.assertEqual(total_profit, expected_total_profit)
        self.assertEqual(solution, expected_solution)

if __name__ == "__main__":
    unittest.main()
