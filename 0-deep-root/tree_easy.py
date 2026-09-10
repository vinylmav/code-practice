from tree import a, b, c, d, e, f, g, h, i , j

def sum(node):
    if node is None:
        return 0
    return node.value + sum(node.left) + sum(node.right)

def count_leaf_nodes(node):
    if node is None:
        return 0
    if node.left is None and node.right is None:
        return 1
    return count_leaf_nodes(node.left) + count_leaf_nodes(node.right)

# print(min_depth(a))

