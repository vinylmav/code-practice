supplies = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
target = 10
n = len(supplies)
l = 0
sum_of_window = 0
min_length = 10**5 + 1
for r in range(n):
    sum_of_window += supplies[r]
    while l <= r and sum_of_window >= target:
        min_length = min(min_length, r - l + 1)
        sum_of_window -= supplies[l]
        l += 1
print(min_length)
