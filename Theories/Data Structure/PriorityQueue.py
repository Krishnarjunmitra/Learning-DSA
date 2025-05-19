"""
Priority Queue Data Structure: Theory and Implementation (using heapq)
"""
import heapq

class PriorityQueue:
    def __init__(self):
        self.heap = []

    def push(self, item):
        heapq.heappush(self.heap, item)

    def pop(self):
        if not self.heap:
            raise IndexError("pop from empty priority queue")
        return heapq.heappop(self.heap)

    def peek(self):
        if not self.heap:
            raise IndexError("peek from empty priority queue")
        return self.heap[0]

    def size(self):
        return len(self.heap)

'''
Use Cases:
- Task scheduling (OS process scheduling)
- Dijkstra's shortest path algorithm
- Bandwidth management (network packets)
- Event-driven simulation
'''
