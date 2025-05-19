"""
Exponential Search: Theory and Implementation
"""

def exponential_search(arr, target):
    if arr[0] == target:
        return 0
    i = 1
    n = len(arr)
    while i < n and arr[i] <= target:
        i *= 2
    return binary_search(arr[:min(i, n)], target)

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

'''
Use Cases:
- Searching in unbounded or infinite lists
- Large sorted arrays
- Real-time systems
'''
