"""
Tree Algorithms: Theory and Implementation
"""

def inorder_traversal(root):
    return inorder_traversal(root.left) + [root.value] + inorder_traversal(root.right) if root else []

def preorder_traversal(root):
    return [root.value] + preorder_traversal(root.left) + preorder_traversal(root.right) if root else []

def postorder_traversal(root):
    return postorder_traversal(root.left) + postorder_traversal(root.right) + [root.value] if root else []

'''
Use Cases:
- Expression evaluation
- File system traversal
- Syntax tree processing
- Hierarchical data analysis
'''
