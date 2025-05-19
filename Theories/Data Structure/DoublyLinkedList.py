"""
Doubly Linked List Data Structure: Theory and Implementation
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = self.tail = new_node
            return
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

'''
Use Cases:
- Browser history navigation (back and forward)
- Undo/redo functionality in editors
- Implementation of LRU cache
- Playlist navigation
'''
