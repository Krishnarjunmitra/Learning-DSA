"""
Sublist Search: Theory and Implementation
"""

def sublist_search(lst, sub):
    n, m = len(lst), len(sub)
    for i in range(n - m + 1):
        if lst[i:i+m] == sub:
            return i
    return -1

'''
Use Cases:
- Pattern matching in lists
- DNA sequence analysis
- Searching for subarrays in arrays
'''
