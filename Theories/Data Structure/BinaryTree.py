"""
Binary Tree Data Structure: Theory and Implementation
"""

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root_value):
        self.root = TreeNode(root_value)

    def insert_left(self, current_node, value):
        current_node.left = TreeNode(value)
        return current_node.left

    def insert_right(self, current_node, value):
        current_node.right = TreeNode(value)
        return current_node.right

'''
Use Cases:
- Hierarchical data (file systems, organization charts)
- Expression parsing (expression trees)
- Binary search trees for fast lookup, insert, delete
- Huffman coding trees for compression
'''
