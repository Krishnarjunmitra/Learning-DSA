"""
String Data Structure: Theory and Implementation
"""

class String:
    def __init__(self, value):
        self.value = value

    def __len__(self):
        return len(self.value)

    def __getitem__(self, idx):
        return self.value[idx]

    def substring(self, start, end):
        return self.value[start:end]

    def concat(self, other):
        return self.value + other.value

'''
Use Cases:
- Text processing (search, replace, split)
- Data parsing (CSV, JSON)
- Pattern matching (regex, search engines)
- Cryptography (hashing, encoding)
'''
