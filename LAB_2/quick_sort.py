import random

def quick_sort(arr, p, r):
    if p < r:
        q = randomized_partition(arr, p, r)
        quick_sort(arr, p, q - 1)
        quick_sort(arr, q + 1, r)
        
def randomized_partition(arr, p, r):
    i = random.randint(p, r)
    arr[i], arr[r] = arr[r], arr[i]
    return partition(arr, p, r)

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def partition(arr, p, r):
    pivot = arr[r]
    i = p - 1
    for j in range(p, r):
        if arr[j] <= pivot:
            i += 1
            swap(arr, i, j)
    swap(arr, i + 1, r)
    return i + 1

# arr = [5, 2, 9, 1, 7]
# p = 0
# r = len(arr) - 1
# quick_sort(arr, p, r)
# print(arr)
