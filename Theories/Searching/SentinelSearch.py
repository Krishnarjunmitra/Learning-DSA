"""
Sentinel Search: Theory and Implementation
"""

def sentinel_search(arr, target):
    n = len(arr)
    last = arr[-1]
    arr[-1] = target
    i = 0
    while arr[i] != target:
        i += 1
    arr[-1] = last
    if i < n - 1 or arr[-1] == target:
        return i
    return -1

'''
Use Cases:
- Optimized linear search
- Reducing number of comparisons
- Embedded systems
'''
