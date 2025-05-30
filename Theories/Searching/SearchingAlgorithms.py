"""
Searching Algorithms: Theory and Implementation
"""

def linear_search(arr, target):
    for i, value in enumerate(arr):
        if value == target:
            return i
    return -1

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
- Finding elements in a list or database
- Dictionary word lookup
- Real-time search in sorted data (binary search)
- Pattern matching (searching substrings)
'''
