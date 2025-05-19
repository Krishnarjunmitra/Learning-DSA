"""
Block Search (Index Sequential Search): Theory and Implementation
"""

def block_search(arr, target, block_size):
    n = len(arr)
    i = 0
    while i < n and arr[min(i + block_size - 1, n - 1)] < target:
        i += block_size
    for j in range(i, min(i + block_size, n)):
        if arr[j] == target:
            return j
    return -1

'''
Use Cases:
- Large databases (indexing)
- Searching in blocks (disk storage)
- Hybrid search techniques
'''
