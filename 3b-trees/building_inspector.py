from tree_node import *

depth_seen = set()

def building_inspector_dfs(node, depth, r_view, depth_seen):
    if node is None:
        return []
    if depth not in depth_seen:
        r_view.append(node.value)
    depth_seen.add(depth)
    building_inspector_dfs(node.right, depth + 1, r_view, depth_seen)
    building_inspector_dfs(node.left, depth + 1, r_view, depth_seen)
    return r_view

def building_inspector_bfs(node, r_view):
    from collections import deque
    if node is None:
        return []
    queue = deque([node])
    while queue:
        level_length = len(queue)
        level = []
        for _ in range(level_length):
            current = queue.popleft()
            level.append(current.value)
            if current.left is not None:
                queue.append(current.left)
            if current.right is not None:
                queue.append(current.right)
        r_view.append(level[-1])
    return r_view

print(building_inspector_dfs(tree_d(), 0, [], depth_seen))
