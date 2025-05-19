"""
Circular Queue Data Structure: Theory and Implementation
"""

class CircularQueue:
    def __init__(self, k):
        self.queue = [None] * k
        self.max_size = k
        self.front = self.rear = -1

    def enqueue(self, value):
        if ((self.rear + 1) % self.max_size == self.front):
            raise IndexError("Queue is full")
        elif self.front == -1:
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.max_size
        self.queue[self.rear] = value

    def dequeue(self):
        if self.front == -1:
            raise IndexError("Queue is empty")
        value = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.max_size
        return value

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.max_size == self.front

'''
Use Cases:
- CPU scheduling (round-robin)
- Streaming data buffers
- Traffic management (circular buffer)
- Resource pool management
'''
