"""
Hashing Techniques: Theory and Implementation
"""

# Open Addressing (Linear Probing)
class OpenAddressingHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size
    def hash(self, key):
        return hash(key) % self.size
    def insert(self, key, value):
        idx = self.hash(key)
        while self.table[idx] is not None:
            idx = (idx + 1) % self.size
        self.table[idx] = (key, value)
    def search(self, key):
        idx = self.hash(key)
        start = idx
        while self.table[idx] is not None:
            if self.table[idx][0] == key:
                return self.table[idx][1]
            idx = (idx + 1) % self.size
            if idx == start:
                break
        return None

# Chaining
class ChainingHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]
    def hash(self, key):
        return hash(key) % self.size
    def insert(self, key, value):
        idx = self.hash(key)
        self.table[idx].append((key, value))
    def search(self, key):
        idx = self.hash(key)
        for k, v in self.table[idx]:
            if k == key:
                return v
        return None

'''
Use Cases:
- Implementing dictionaries/maps
- Caching
- Database indexing
- Load balancing
'''
