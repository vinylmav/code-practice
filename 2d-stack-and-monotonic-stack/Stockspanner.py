class StockSpanner:

    def __init__(self):
        self.stack = [(100, 1)]

    def next(self, price):
        n = len(self.stack)
        for i in range(n):
            print("i", i)
            span = 1
            print(self.stack)
            while self.stack and self.stack[-1][0] < price:
                span += self.stack.pop()[-1]
            self.stack.append((price, span))
            print("*" * 20)
        return self.stack[-1][-1]

spanner = StockSpanner()
# print(spanner.next(100))  # → 1
print(spanner.next(80))   # → 1
print(spanner.next(60))   # → 1
print(spanner.next(70))   # → 2
print(spanner.next(60))   # → 1
print(spanner.next(75))   # → 4
print(spanner.next(85))   # → 6
