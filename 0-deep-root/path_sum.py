from trees import a

balance = []
def path_sum(node, coins):
    if node is None:
        balance.append(coins)
        return
    path_sum(node.left, coins - node.value)
    path_sum(node.right, coins - node.value)

path_sum(a, 7)

if any(b == 0 for b in balance):
    print("Path exists!")
