"""
Heap Data Structure: Theory and Implementation (Min Heap)
"""
import heapq

class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, item):
        heapq.heappush(self.heap, item)

    def pop(self):
        if not self.heap:
            raise IndexError("pop from empty heap")
        return heapq.heappop(self.heap)

    def peek(self):
        if not self.heap:
            raise IndexError("peek from empty heap")
        return self.heap[0]

    def size(self):
        return len(self.heap)

'''
Use Cases:
- Priority queues
- Heap sort
- Finding the k largest/smallest elements
- Graph algorithms (Dijkstra, Prim)
'''
