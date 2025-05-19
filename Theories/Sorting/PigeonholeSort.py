"""
Pigeonhole Sort: Theory and Implementation
"""

def pigeonhole_sort(arr):
    if not arr:
        return arr
    min_val, max_val = min(arr), max(arr)
    size = max_val - min_val + 1
    holes = [0] * size
    for x in arr:
        holes[x - min_val] += 1
    i = 0
    for count in range(size):
        while holes[count] > 0:
            arr[i] = count + min_val
            i += 1
            holes[count] -= 1
    return arr

'''
Use Cases:
- Sorting integers in a small range
- Distribution sort
- Data analysis
'''
