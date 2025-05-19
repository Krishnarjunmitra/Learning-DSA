"""
Data Compression Algorithms: Theory and Implementation
"""
import heapq
from collections import Counter, namedtuple

# Huffman Coding (basic)
class Node(namedtuple("Node", ["char", "freq", "left", "right"])):
    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(text):
    freq = Counter(text)
    heap = [Node(ch, fr, None, None) for ch, fr in freq.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        heapq.heappush(heap, Node(None, left.freq + right.freq, left, right))
    return heap[0] if heap else None

# Run-Length Encoding (basic)
def run_length_encode(s):
    encoded = ""
    i = 0
    while i < len(s):
        count = 1
        while i + 1 < len(s) and s[i] == s[i+1]:
            i += 1
            count += 1
        encoded += s[i] + str(count)
        i += 1
    return encoded

'''
Use Cases:
- File compression (ZIP, PNG, MP3)
- Data transmission
- Reducing storage requirements
- Text and image encoding
'''
