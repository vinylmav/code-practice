import math

from tree_node import TreeNode, tree_a, tree_f, tree_b, tree_c, tree_d, tree_h, tree_i

# Drill 1: Build a tree by hand and walk it
tree1 = TreeNode(1,
    TreeNode(2,
        TreeNode(4), TreeNode(5)
    ), TreeNode(3,
        None, TreeNode(6)
    )
)

# Drill 2: Count nodes
def count(node):
    if node is None:
        return 0
    return 1 + count(node.left) + count(node.right)

# Drill 3: Sum of all nodes
def sum_nodes(node):
    if node is None:
        return 0
    return node.value + sum_nodes(node.left) + sum_nodes(node.right)

# Drill 4: Height of tree
def height(node):
    if node is None:
        return 0
    return 1 + max(height(node.left), height(node.right))

# Drill 5: Max value in tree
def max_value(node):
    if node is None:
        return -math.inf
    return max(node.value, max_value(node.left), max_value(node.right))

# Drill 6: Are two trees identical?
def same_tree(node1, node2):
    if node1 is None and node2 is None:
        return True
    if (node1 is None and node2 is not None) or (node1 is not None and node2 is None):
        return False
    if node1.value != node2.value:
        return False
    return same_tree(node1.left, node2.left) and same_tree(node1.right, node2.right)

# Drill 7: Are two trees mirror images?
def mirror_tree(node1, node2):
    if node1 is None and node2 is None:
        return True
    if (node1 is None and node2 is not None) or (node1 is not None and node2 is None):
        return False
    if node1.value != node2.value:
        return False
    return mirror_tree(node1.left, node2.right) and mirror_tree(node1.right, node2.left)


# Drill 8: Is tree symmetric?
def is_symmetric(node):
    if node is None:
        return True
    return mirror_tree(node.left, node.right)

print(is_symmetric(tree_c()))
