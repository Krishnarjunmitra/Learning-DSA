"""
Persistent Data Structures: Theory and Implementation
"""

# Persistent Stack (simple version)
class PersistentStack:
    def __init__(self, prev=None, value=None):
        self.prev = prev
        self.value = value
    def push(self, value):
        return PersistentStack(self, value)
    def pop(self):
        return self.prev
    def top(self):
        return self.value

'''
Use Cases:
- Undo operations
- Functional programming
- Version control systems
- Time-travel debugging
'''
