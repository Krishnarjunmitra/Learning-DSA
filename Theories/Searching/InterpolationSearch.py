"""
Interpolation Search: Theory and Implementation
"""

def interpolation_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high and arr[low] <= target <= arr[high]:
        if low == high:
            if arr[low] == target:
                return low
            return -1
        pos = low + ((high - low) * (target - arr[low])) // (arr[high] - arr[low])
        if arr[pos] == target:
            return pos
        if arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1
    return -1

'''
Use Cases:
- Fast search in uniformly distributed sorted arrays
- Large databases (indexing)
- Applications where binary search is not optimal
'''
