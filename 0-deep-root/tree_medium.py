from copy import deepcopy
import math
from tree import a, b, c, d, e, f, g, h, i, j, h

def min_depth(node):
    if node is None:
        return math.inf
    if node.left is None and node.right is None:
        return 1
    return 1 + min(min_depth(node.left), min_depth(node.right))

def root_to_leaf(node, path):
    if node is None:
        print('', end='')
        return
    if node.left is None and node.right is None:
        print(f'{path}{node.value}')
        return
    root_to_leaf(node.left, path+f'{node.value}->')
    root_to_leaf(node.right, path+f'{node.value}->')

def same_tree(a, b):
    if a is None and b is None:
        return True
    if a is None or b is None:
        return False
    if a.value == b.value:
        return same_tree(a.left, b.left) and same_tree(a.right, b.right)
    return False

def mirror(node):
    if node is None:
        return None
    node.left, node.right = mirror(node.right), mirror(node.left)
    return node

def Symmetric(node):
    """Symmetric -> mirror and check whether the mirrored one
    is identical to the original one"""
    # original = node
    # but this is a classic python referencing trap, so use deepcopy
    mirrored = mirror(node)
    original = deepcopy(node)
    return same_tree(original, mirrored)

def symmetric(node):
    if node is None:
        return False
    if node.left is None and node.right is None:
        return True
    return symmetric(node.left) and symmetric(node.right)

def sum_of_left_leaves(node, dir):
    if node is None:
        return 0
    if node.left is None and node.right is None and dir == 'l':
            return node.value
    return sum_of_left_leaves(node.left, 'l') + sum_of_left_leaves(node.right, 'r')

def is_balanced(node):
    if node is None:
        return 0
    left_height = 1 + is_balanced(node.left)
    right_height = 1 + is_balanced(node.right)
    if abs(left_height - right_height) > 1:
        return -1
    return max(left_height, right_height)

# print(root_to_leaf(f, ''))
# print(root_to_leaf(mirror(f), ''))
# print(symmetric(f))
# print(Symmetric(f))
# print(sum_of_left_leaves(h, ''))
print(is_balanced(f))
