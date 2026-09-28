class MyQueue:

    def __init__(self):
        self.front = []
        self.back = []

    def push(self, x):
        self.back.append(x)

    def pop(self):
        if not self.front:
            while self.back:
                self.front.append(self.back.pop())
        return self.front.pop()

    def peek(self):
        if not self.front:
            while self.back:
                self.front.append(self.back.pop())
        return self.front[-1]

    def empty(self):
        return not self.front and not self.back

q = MyQueue()
q.push(1)    # queue: [1]
q.push(2)    # queue: [1, 2]
print(q.peek())     # → 1
print(q.pop())      # → 1,  queue: [2]
print(q.empty())    # → False
