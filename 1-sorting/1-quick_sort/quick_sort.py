#!/usr/bin/env python3

import time

def quickSort(arr):
    # base case
    if (len(arr) <= 1): return arr

    pivot = arr[-1] #choose right most pivot
    arr = arr[:-1] #remove pivot from array
    left = []
    right = []

    for num in arr:
        # Add elemnts < pivot to left
        if num < pivot: left.append(num)
        # Add elements > pivot to right
        else: right.append(num)

    return quickSort(left) + [pivot] + quickSort(right)


test_arrays = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],  # All elements are the same
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],  # Already sorted array
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],  # Reverse sorted array
    [1, 2, 3, 4, 5, 1, 2, 3, 4, 5],  # Repeated pattern
    [1, 3, 2, 4, 6, 5, 7, 9, 8, 10],  # Nearly sorted array
    [10, 1, 9, 2, 8, 3, 7, 4, 6, 5],  # Alternating high-low pattern
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 1],  # Sorted with one outlier at the end
    [1, 9, 1, 9, 1, 9, 1, 9, 1, 9],  # Alternating low-high pattern
    [5, 5, 5, 5, 5, 1, 1, 1, 1, 1],  # Half same elements, half different
    [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]   # Repeated small pattern
]

for i, test_arr in enumerate(test_arrays):
    print(f"Test array {i+1}: {test_arr}")
    print(f"Sorted: {quickSort(test_arr)}\n")
