from tree_node import *

def family_ancestor(node, p, q):
    if node is None:
        return False
    l = family_ancestor(node.left, p, q)
    r = family_ancestor(node.right, p, q)
    if type(l) is int:
        return l
    if type(r) is int:
        return r
    if l and r:
        return node.value
    c = node.value == p or node.value == q
    if (l or r) and c:
        return node.value
    if node.value == p or node.value == q:
        return True
    if l or r:
        return True
    return False

print(family_ancestor(tree_g(), 2, 14))
