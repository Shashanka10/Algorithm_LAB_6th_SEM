import numpy as np
import matplotlib.pyplot as plt
from selection_sort import selection_sort
from insertion_sort import insertion_sort
import time

def gen_Array(n: int):
    return [np.random.randint(0, 100000) for _ in range(n)]

def comparison(n: int):
    arr = gen_Array(n)
    
    begin = time.time()
    insertion_sort(arr)
    end = time.time()
    insertion_time = end - begin

    begin = time.time()
    selection_sort(arr)
    end = time.time()
    selection_time = end - begin

    return insertion_time, selection_time

def main():
    sizes = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
    insertion_times = []
    selection_times = []

    for size in sizes:
        insertion_time, selection_time = comparison(size)
        insertion_times.append(insertion_time)
        selection_times.append(selection_time)

    plt.plot(sizes, insertion_times, label='Insertion Sort')
    plt.plot(sizes, selection_times, label='Selection Sort')
    plt.xlabel('Size of an Array')
    plt.ylabel('Time (in seconds)')
    plt.title('Comparison of Insertion Sort and Selection Sort')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()