"""
Hash Map Data Structure: Theory and Implementation (using Python dict)
"""

class HashMap:
    def __init__(self):
        self.map = {}

    def put(self, key, value):
        self.map[key] = value

    def get(self, key):
        return self.map.get(key, None)

    def remove(self, key):
        if key in self.map:
            del self.map[key]

    def contains_key(self, key):
        return key in self.map

'''
Use Cases:
- Caching (storing computed results for fast lookup)
- Counting frequencies (word count, character count)
- Implementing sets and dictionaries
- Indexing data for fast retrieval
'''
