"""
Deque (Double-Ended Queue) Data Structure: Theory and Implementation
"""

class Deque:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def add_front(self, item):
        self.items.insert(0, item)

    def add_rear(self, item):
        self.items.append(item)

    def remove_front(self):
        if self.is_empty():
            raise IndexError("remove from empty deque")
        return self.items.pop(0)

    def remove_rear(self):
        if self.is_empty():
            raise IndexError("remove from empty deque")
        return self.items.pop()

    def size(self):
        return len(self.items)

'''
Use Cases:
- Palindrome checking
- Sliding window problems
- Undo/redo operations
- Task scheduling (both ends)
'''
