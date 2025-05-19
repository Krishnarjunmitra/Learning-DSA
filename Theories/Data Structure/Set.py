"""
Set Data Structure: Theory and Implementation (using Python set)
"""

class Set:
    def __init__(self):
        self.set = set()

    def add(self, item):
        self.set.add(item)

    def remove(self, item):
        self.set.remove(item)

    def contains(self, item):
        return item in self.set

    def union(self, other_set):
        return self.set.union(other_set.set)

    def intersection(self, other_set):
        return self.set.intersection(other_set.set)

    def difference(self, other_set):
        return self.set.difference(other_set.set)

'''
Use Cases:
- Removing duplicates from a collection
- Membership testing (fast lookup)
- Mathematical set operations (union, intersection)
- Graph algorithms (visited nodes)
'''
