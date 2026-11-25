from tree_node import *

root = tree_g()

def count(node):
    if node is None:
        return 0
    return 1 + count(node.left) + count(node.right)

def sum_node(node):
    if node is None:
        return 0
    return node.value + sum_node(node.left) + sum_node(node.right)

def height(node):
    if node is None:
        return 0
    return 1 + max(height(node.left), height(node.right))

def maximum(node):
    if node is None:
        return 0
    return max(node.value, maximum(node.left), maximum(node.right))

def same_tree(a, b):
    if a is None and b is None:
        return True
    if (a is None and b is not None) or (a is not None and b is None):
        return False
    return (a.value == b.value) and same_tree(a.left, b.left) and same_tree(a.right, b.right)

