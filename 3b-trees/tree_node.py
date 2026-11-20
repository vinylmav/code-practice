class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f"TreeNode({self.value})"


# ── Test Trees ──────────────────────────────────────────

# Tree A — Standard (balanced-ish)
#       1
#      / \
#     2   3
#    / \   \
#   4   5   6

def tree_a():
    return TreeNode(1,
        TreeNode(2, TreeNode(4), TreeNode(5)),
        TreeNode(3, None, TreeNode(6)))

# Tree B — Single Node
def tree_b():
    return TreeNode(42)

# Tree C — Empty
def tree_c():
    return None

# Tree D — Left-Skewed
#         1 
#        /
#       2
#      /
#     3
#    /
#   4
def tree_d():
    return TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4))))

# Tree E — Right-Skewed
# 1
#  \
#   2
#    \
#     3
def tree_e():
    return TreeNode(1, None, TreeNode(2, None, TreeNode(3)))

# Tree F — Perfect Binary Tree
#         1
#        / \
#       2    3
#      / \  / \
#     4  5 6   7
def tree_f():
    return TreeNode(1,
        TreeNode(2, TreeNode(4), TreeNode(5)),
        TreeNode(3, TreeNode(6), TreeNode(7)))

# Tree G — BST
#         8
#        / \
#       4   12
#      / \  / \
#     2  6 10  14
def tree_g():
    return TreeNode(8,
        TreeNode(4, TreeNode(2), TreeNode(6)),
        TreeNode(12, TreeNode(10), TreeNode(14)))

# Tree H — Symmetric
#       1
#      / \
#     2   2
#    / \ / \
#   3  4 4  3
def tree_h():
    return TreeNode(1,
        TreeNode(2, TreeNode(3), TreeNode(4)),
        TreeNode(2, TreeNode(4), TreeNode(3)))

# Tree I — NOT Symmetric
#       1
#      / \
#     2   2
#      \   \
#       3   3
def tree_i():
    return TreeNode(1,
        TreeNode(2, None, TreeNode(3)),
        TreeNode(2, None, TreeNode(3)))

# Tree J — Unbalanced
#         1
#        /
#       2
#      / \
#     3   4
#    /
#   5
def tree_j():
    return TreeNode(1,
        TreeNode(2,
            TreeNode(3, TreeNode(5)),
            TreeNode(4)))
