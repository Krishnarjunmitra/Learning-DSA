"""
Self-Organizing Search: Theory and Implementation
"""

def move_to_front_search(arr, target):
    for i, value in enumerate(arr):
        if value == target:
            arr.insert(0, arr.pop(i))
            return 0
    return -1

'''
Use Cases:
- Frequently accessed elements
- Caching and memory management
- Adaptive data structures
'''
