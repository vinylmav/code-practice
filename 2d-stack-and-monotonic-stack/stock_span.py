prices = [1, 2, 3, 4, 5]
# [1000, 300, 100, 10, 200, 900]
def stock_span(prices):
    n = len(prices)
    spans = [1] * n
    stack = [0]
    for i in range(1, n):
        placer = 1
        while stack and prices[stack[-1]] <= prices[i]:
            placer += spans[stack.pop()]
        stack.append(i)
        spans[i] = placer
    return spans

print(stock_span(prices))
