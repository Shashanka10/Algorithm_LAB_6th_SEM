import unittest

#Solves the 0/1 knapsack problem using dynamic programming with memoization
def dynamic_01_knapsack(profits, weights, capacity):

    n = len(weights)
    memo = [[-1 for j in range(capacity + 1)] for i in range(n)]

    def knapsack_recursive(i, capacity):
        if i == n:
            return 0
        if memo[i][capacity] != -1:
            return memo[i][capacity]
        if weights[i] > capacity:
            memo[i][capacity] = knapsack_recursive(i + 1, capacity)
        else:
            memo[i][capacity] = max(
                knapsack_recursive(i + 1, capacity),
                profits[i] + knapsack_recursive(i + 1, capacity - weights[i]),
            )
        return memo[i][capacity]

    max_profit = knapsack_recursive(0, capacity)
    solution = []

    # Determine selected items
    current_capacity = capacity
    for i in range(n):
        if knapsack_recursive(i, current_capacity) != knapsack_recursive(i + 1, current_capacity):
            solution.append((profits[i], weights[i]))
            current_capacity -= weights[i]

    return max_profit, solution

profits = [60, 100, 120]
weights = [10, 20, 30]
capacity = 30
max_profit, solution = dynamic_01_knapsack(profits, weights, capacity)

print("Maximum Profit is:", max_profit)
print("The solution are:")
for profit, weight in solution:
    print(f"Item with profit {profit} and weight {weight} is taken")

# Unit tests for the dynamic_01_knapsack function
class TestKnapsack(unittest.TestCase):

    def test_dynamic_01_knapsack(self):
        
        expected_max_profit = 160
        expected_solution = [
            (60, 10), 
            (100, 20),
            (120, 30)
        ]
        self.assertEqual(max_profit, expected_max_profit)
        self.assertEqual(solution, expected_solution)

if __name__ == "__main__":
    unittest.main()
