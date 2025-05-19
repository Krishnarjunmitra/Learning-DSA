"""
Gnome Sort: Theory and Implementation
"""

def gnome_sort(arr):
    n = len(arr)
    index = 0
    while index < n:
        if index == 0 or arr[index] >= arr[index - 1]:
            index += 1
        else:
            arr[index], arr[index - 1] = arr[index - 1], arr[index]
            index -= 1
    return arr

'''
Use Cases:
- Simple sorting for small arrays
- Educational purposes
- Adaptive sorting
'''
