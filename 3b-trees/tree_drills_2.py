from tree_node import *

ps = TreeNode(5,
    TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))),
    TreeNode(8, TreeNode(13), TreeNode(4, None, TreeNode(1))))

# Drill 9: Has Path Sum
def path_sum(node, target):
    if node is None:
        return False
    target -= node.value
    if node.left is None and node.right is None:
        return target == 0
    return path_sum(node.left, target) or path_sum(node.right, target)
# first subtract (you can do so with the parameter itself), then check.
# you didn't subtract the leaf node's value before checking. that's the error.

# Drill 10: All Root-to-Leaf Paths
def all_paths(node):
    def helper(node, path, results):
        if node is None:
            return
        if node.left is None and node.right is None:
            path.append(f"{node.value}")
            results.append(''.join(path))
            path.pop()
            return results
        path.append(f"{node.value}->")
        helper(node.left, path, results)
        helper(node.right, path, results)
        path.pop()
        return results
    return helper(node, [], [])

def find_depth(node, target, depth):
    if node is None:
        return -1
    depth += 1
    if node.value == target:
        return depth
    return max(find_depth(node.left, target, depth), find_depth(node.right, target, depth))

# DFS Traversal

# Drill 12: Pre-order → list
def pre_order(node, order):
    if node is None:
        return
    order.append(node.value)
    pre_order(node.left, order)
    pre_order(node.right, order)
    return order

def post_order(node, order):
    if node is None:
        return
    post_order(node.left, order)
    post_order(node.right, order)
    order.append(node.value)
    return order

def in_order(node, order):
    if node is None:
        return
    in_order(node.left, order)
    order.append(node.value)
    in_order(node.right, order)
    return order

# Drill 15: Level-order flat
from collections import deque

def level_order(node):
    if node is None:
        print('')
        return
    result = []
    queue = deque([node])
    while queue:
        current = queue.popleft()
        result.append(current.value)
        if current.left is not None:
            queue.append(current.left)
        if current.right is not None:
            queue.append(current.right)
    return result

# Drill 16: Level-order grouped
def level_order_grouped(node):
    from collections import deque
    if node is None:
        return []
    result = []
    queue = deque([node])
    while queue:
        level = []
        level_size = len(queue)
        for _ in range(level_size):
            current = queue.popleft()
            level.append(current.value)
            if current.left is not None:
                queue.append(current.left)
            if current.right is not None:
                queue.append(current.right)
        result.append(level)
    return result

# Drill 17: Is Balanced?
def is_balanced(node):
    if node is None:
        return 1
    left_height = is_balanced(node.left)
    right_height = is_balanced(node.right)
    if left_height == -1 or right_height == -1:
        return -1
    diff = abs(left_height - right_height)
    if diff > 1:
        return -1
    return 1 + max(left_height, right_height)

ans = is_balanced(tree_d())

# Drill 18: Diameter
def diameter(node):
    if node is None:
        return [0, 0]
    lh, ld = diameter(node.left)
    rh, rd = diameter(node.right)
    return [1 + max(lh, rh), max(ld, rd, lh + rh)]

