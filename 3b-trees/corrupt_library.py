import math

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f"TreeNode({self.value})"


# Tree 1: Valid BST -> True
#       2
#      / \
#     1   3

root1 = TreeNode(2)
root1.left = TreeNode(1)
root1.right = TreeNode(3)


# Tree 2: Invalid BST -> False
#       5
#      / \
#     1   4
#        / \
#       3   6

root2 = TreeNode(5)
root2.left = TreeNode(1)
root2.right = TreeNode(4)
root2.right.left = TreeNode(3)
root2.right.right = TreeNode(6)


# Tree 3: Invalid BST -> False
#       5
#      / \
#     4   6
#        / \
#       3   7

root3 = TreeNode(5)
root3.left = TreeNode(4)
root3.right = TreeNode(6)
root3.right.left = TreeNode(3)
root3.right.right = TreeNode(7)


# Tree 4: Single Node -> True
#       1

root4 = TreeNode(1)

# All test cases
trees = [root1, root2, root3, root4]

def corrupt_library(node):
    if node is None:
        return True
    def helper(node, l_min, r_max):
        if node is None:
            return True
        if not (l_min < node.value < r_max):
            return False
        l = helper(node.left, l_min, node.value)
        r = helper(node.right, node.value, r_max)
        return l and r
    lim = node.value
    return helper(node.left, -math.inf, lim) and helper(node.right, lim, math.inf)

for root in trees:
    print(corrupt_library(root))
