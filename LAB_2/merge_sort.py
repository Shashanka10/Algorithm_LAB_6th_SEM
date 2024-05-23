import math
def merge_sort(arr, p, r):
    if p < r:
        mid = (p + r) // 2
        merge_sort(arr, p, mid)
        merge_sort(arr, mid + 1, r)
        merge(arr, p, mid, r) 
        
def merge(arr, p, mid, r):
    n1 = mid - p + 1
    n2 = r - mid 
    L = [0] * (n1 + 1)
    R = [0] * (n2 + 1) 
 
    for i in range(n1):
        L[i] = arr[p + i]
    for j in range(n2):
        R[j] = arr[mid + 1 + j]
    
    L[n1] = math.inf
    R[n2] = math.inf
    i = j = 0
    
    for k in range(p, r + 1):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1

# arr = [4, 2, 7, 1, 5, 3]
# p = 0
# r = len(arr) - 1
# merge_sort(arr, p, r)
# print(arr)
