scores = [1, 1, 1, 1, 5]
k = 1
n = len(scores)
l = 0
running_total = sum(scores[:k])
max_total = running_total
for r in range(k, n):
    running_total = running_total - scores[l] + scores[r]
    max_total = max(running_total, max_total)
    l += 1
print(max_total)
