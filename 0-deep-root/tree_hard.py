from tree import a, TreeNode

def lca(node, a, b):
    if node is None:
        return None
    left_subtree = lca(node.left, a, b)
    # if left_subtree is not None:
    #     print(f'Left of {node.value} is {left_subtree.value}')
    # else:
    #     print(f'Left of {node.value} is {None}')
    # motherfucking goddamn mistake i made . i just wrote node.left instead of node.right
    right_subtree = lca(node.right, a, b)
    # if right_subtree is not None:
    #     print(f'Right of {node.value} is {right_subtree.value}')
    # else:
    #     print(f'Right of {node.value} is {None}')
    c1 = left_subtree is not None
    c2 = right_subtree is not None
    c3 = node.value == a
    c4 = node.value == b
    if c1 and c2:
        return node
    if (c1 or c2) and (c3 or c4):
        return node
    if c1:
        return left_subtree
    if c2:
        return right_subtree
    if c3 or c4:
        return node
    return None

ans = lca(a, 4, 2)
# if ans is not None:
    # print(ans.value)
