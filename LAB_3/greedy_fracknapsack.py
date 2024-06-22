import unittest

class Item:
    def __init__(self, profit, weight):
        self.profit = profit
        self.weight = weight
        self.ratio = profit / weight

def greedy_fractional_knapSack(profits, weights, capacity):
    assert len(profits) == len(weights), "Length of profits and weights must be the same"
    
    n = len(profits)
    items = []
    
    # Create list of Item objects
    for i in range(n):
        items.append(Item(profits[i], weights[i]))
    
    # Sort items based on profit-to-weight ratio in descending order
    items.sort(key=lambda x: x.ratio, reverse=True)
    
    total_profit = 0
    total_weight = 0
    solution = []
    
    for item in items:
        if total_weight + item.weight <= capacity:
            # Take the whole item
            total_profit += item.profit
            total_weight += item.weight
            solution.append((item.profit, item.weight, 1))  # 1 means the full item is taken
        else:
            # Take a fraction of the remaining capacity
            remaining_capacity = capacity - total_weight
            fraction = remaining_capacity / item.weight
            total_profit += item.profit * fraction
            total_weight += item.weight * fraction
            solution.append((item.profit, item.weight, fraction))  # fraction taken
            break  # Knapsack is full
    
    return total_profit, solution

# Example usage:
profits = [60, 100, 120]
weights = [10, 20, 30]
max_capacity = 50

max_profit, solution = greedy_fractional_knapSack(profits, weights, max_capacity)
print("Maximum Profit is:", max_profit)
print("The solution is:")
for profit, weight, fraction in solution:
    print(f"Item with profit {profit} and weight {weight} is taken with fraction {fraction}")


class TestFractionalKnapsack(unittest.TestCase):
    def test_greedy_fractional_knapsack(self):
        expected_max_profit = 240  # 100 from item 1 + 120 from item 2 + 20 from half of item 3
        expected_solution = [
            (60, 10, 1),  # Full item 1
            (100, 20, 1),  # Full item 2
            (120, 30, 1/3)  # 1/3 of item 3
        ]
        
        max_profit,solution = greedy_fractional_knapSack(profits, weights, max_capacity)
        self.assertEqual(max_profit, expected_max_profit)
        self.assertEqual(solution, expected_solution)

if __name__ == "__main__":
    unittest.main()


