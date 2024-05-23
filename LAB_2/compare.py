import numpy as np
import matplotlib.pyplot as plt
import time
import sys
import random
from quick_sort import quick_sort
from merge_sort import merge_sort

# Increase the recursion limit
sys.setrecursionlimit(1000000)

# Function to generate a random array of size n
def gen_array(n: int):
    return [np.random.randint(0, 1000000) for _ in range(n)]

# Function to measure execution time
def measure_time(sort_function, arr, p, r):
    start_time = time.time()
    sort_function(arr, p, r)
    end_time = time.time()
    return end_time - start_time

# Function to perform comparisons and gather execution times
def comparison(n: int):
    print(f"Generating and sorting array of size: {n}")
    random_array = gen_array(n)
    sorted_array = sorted(random_array)
    reversed_array = sorted_array[::-1]
    
    # Shuffle the arrays before sorting to avoid worst-case scenarios
    random.shuffle(sorted_array)
    random.shuffle(reversed_array)
    
    # Measure Quick Sort times
    quick_best_time = measure_time(quick_sort, sorted_array[:], 0, n - 1)
    quick_worst_time = measure_time(quick_sort, reversed_array[:], 0, n - 1)
    
    # Measure Merge Sort times
    merge_time = measure_time(merge_sort, random_array[:], 0, n - 1)
    
    return quick_best_time, quick_worst_time, merge_time

def main():
    sizes = list(range(100000, 1900001, 100000))  # Generate sizes from 50 to 2000 in intervals of 50
    quick_best_times = []
    quick_worst_times = []
    merge_times = []

    for size in sizes:
        try:
            quick_best_time, quick_worst_time, merge_time = comparison(size)
            quick_best_times.append(quick_best_time)
            quick_worst_times.append(quick_worst_time)
            merge_times.append(merge_time)
        except Exception as e:
            print(f"Error processing size {size}: {e}")
            break

    # Plot the results
    plt.figure(figsize=(14, 7))
    plt.plot(sizes[:len(quick_best_times)], quick_best_times, label='Quick Sort (Best Case)', marker='o')
    plt.plot(sizes[:len(quick_worst_times)], quick_worst_times, label='Quick Sort (Worst Case)', marker='o')
    plt.plot(sizes[:len(merge_times)], merge_times, label='Merge Sort', marker='o')
    plt.xlabel('Input Size')
    plt.ylabel('Execution Time (seconds)')
    plt.title('Execution Time vs Input Size for Quick Sort and Merge Sort')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
