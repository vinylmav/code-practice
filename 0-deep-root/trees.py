import math


class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def get_value(self):
        print(self.value)

    def set_right_node(self, right):
        self.right = right

    def set_left_node(self, left):
        self.left = left

    def get_right_node(self):
        print(self.right)

    def get_left_node(self):
        print(self.left)

a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
f = TreeNode(6)
a.set_left_node(b)
a.set_right_node(c)
b.set_left_node(d)
b.set_right_node(e)
c.set_right_node(f)

# 3. i access the node 5 from the root, by going to the left node, then right node.

def count_nodes(node):
    """Count all the nodes in a given tree"""
    if node is None:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)

print("No of nodes in the tree:", count_nodes(a))

def max_value(node):
    """We assume that if the tree is empty, then max value is 0"""
    if node is None:
        return 0
    return max(node.value, max_value(node.left), max_value(node.right))

def max_value_2(node):
    """We assume atleast one node is present in the tree"""
    if node.left is None and node.right is None:
        return node.value
    a = b = -math.inf
    if node.left:
        a =  max(node.value, max_value_2(node.left))
    if node.right:
        b =  max(node.value, max_value_2(node.right))
    return max(a, b)

print("Max Value in the tree:", max_value(a))
print("Max Value in the tree:", max_value_2(a))

def find_height(node):
    heights = []
    def height(node, h=0):
        """Find the depth of the deepest leaf"""
        if node is None:
            heights.append(h)
            return
        height(node.left, h+1)
        height(node.right, h+1)
    height(node)
    print("Height of the tree:", max(heights))

def height(node):
    """Find the depth of the deepest leaf"""
    if node is None:
        return 0
    return 1 + max(height(node.left), height(node.right))
print("Height of the tree:", height(a))


def check(a, b):
    """Check if two trees are identical"""
    if a is None and b is None:
        return True
    # if a is None and b is not None:
    #     return False
    # if a is not None and b is None:
    #     return False
    # if you reach this point in the code, you already know they aren't both None.
    #  That means if either one of them is None, it's a guaranteed mismatch
    if a is None or b is None:
        return False
    if a.value == b.value:
        return check(a.left, b.left) and check(a.right, b.right)
    # no need an else block here, beauty of return
    return False

print("Identical Trees?:", check(a, a))

def mirror(node):
    if node is None:
        return None
    node.left, node.right = mirror(node.right), mirror(node.left)
    return node

def path_sum(node, coins):
    if node is None:
        return False
    if node.right is None and node.left is None:
        return coins == node.value
    return path_sum(node.left, coins - node.value) or path_sum(node.right, coins - node.value)

print(path_sum(a, 7))
