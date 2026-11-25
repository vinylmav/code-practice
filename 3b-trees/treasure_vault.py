from tree_node import *

def treasure_vault(node, k):
    def helper(node, result):
        if node is None:
            return []
        helper(node.left, result)
        result.append(node.value)
        helper(node.right, result)
        return result
    return helper(node, [])[k - 1]

print(treasure_vault(tree_g(), 5))