"""
Memory Management: Theory and Implementation
"""

# Reference Counting (basic)
class RefCountedObject:
    def __init__(self, value):
        self.value = value
        self.ref_count = 1
    def add_ref(self):
        self.ref_count += 1
    def release(self):
        self.ref_count -= 1
        if self.ref_count == 0:
            del self.value

# Garbage Collection (conceptual)
def mark_and_sweep(objects):
    marked = set()
    def mark(obj):
        if obj not in marked:
            marked.add(obj)
            for ref in getattr(obj, 'references', []):
                mark(ref)
    for obj in objects:
        if getattr(obj, 'is_root', False):
            mark(obj)
    for obj in objects:
        if obj not in marked:
            del obj

'''
Use Cases:
- Automatic memory management in programming languages
- Preventing memory leaks
- Efficient resource cleanup
- Reference counting in Python, C++
'''
