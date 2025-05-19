"""
Array Data Structure: Theory and Implementation
"""

class Array:
    def __init__(self, size):
        self.size = size
        self.data = [None] * size

    def get(self, index):
        if 0 <= index < self.size:
            return self.data[index]
        raise IndexError("Index out of bounds")

    def set(self, index, value):
        if 0 <= index < self.size:
            self.data[index] = value
        else:
            raise IndexError("Index out of bounds")

'''
Use Cases:
- Storing collections of data (lists, matrices)
- Random access to elements
- Implementing other data structures (heaps, hash tables)
- Image processing (pixel grids)
'''
