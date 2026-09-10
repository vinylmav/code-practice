class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

a = TreeNode(1)
a.left = TreeNode(2, TreeNode(4), TreeNode(5))
a.right = TreeNode(3, None, TreeNode(6))

b = TreeNode(42)

c = None

d = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4))))

e = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))

f = TreeNode(1,
    TreeNode(2, TreeNode(4), TreeNode(5)),
    TreeNode(3, TreeNode(6), TreeNode(7)))

g = TreeNode(8,
    TreeNode(4, TreeNode(2), TreeNode(6)),
    TreeNode(12, TreeNode(10), TreeNode(14)))

h = TreeNode(1,
    TreeNode(2, TreeNode(3), TreeNode(4)),
    TreeNode(2, TreeNode(4), TreeNode(3)))

i = TreeNode(1,
    TreeNode(2, None, TreeNode(3)),
    TreeNode(2, None, TreeNode(3)))

j = TreeNode(1,
    TreeNode(2,
        TreeNode(3, TreeNode(5)),
        TreeNode(4)))
