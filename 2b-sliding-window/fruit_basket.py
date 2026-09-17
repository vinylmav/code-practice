fruits = [1, 2, 1, 2, 3]
n = len(fruits)
max_length = 0
l = 0
seen = 0
fruits_freq = {}
for r in range(n):
    f = fruits[r]
    fruits_freq[f] = fruits_freq.get(f, 0) + 1
    if fruits_freq[f] <= 1:
        seen += 1
    while l < r and seen > 2:
        lf = fruits[l]
        fruits_freq[lf] -= 1
        if fruits_freq[lf] < 1:
            seen -= 1
        l += 1
    max_length = max(max_length, r - l + 1)
print(max_length)
