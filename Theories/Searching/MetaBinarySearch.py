"""
Meta Binary Search: Theory and Implementation
"""

def meta_binary_search(arr, target):
    n = len(arr)
    lg = n.bit_length()
    pos = 0
    for i in range(lg, -1, -1):
        if pos < n and arr[pos] == target:
            return pos
        new_pos = pos | (1 << i)
        if new_pos < n and arr[new_pos] <= target:
            pos = new_pos
    if pos < n and arr[pos] == target:
        return pos
    return -1

'''
Use Cases:
- Fast searching in sorted arrays
- Bit manipulation based search
- Competitive programming
'''
