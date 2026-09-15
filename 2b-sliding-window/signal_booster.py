signal = "BBABBAAABA"
k = 2
n = len(signal)
l, r = 0, 1
used = 0
max_length = 1
while r < n:
    start = signal[l]
    while r < n and (used < k or signal[r] == start):
        if signal[r] != start:
            used += 1
        r += 1
    used = 0
    max_length = max(max_length, r - l)
    l += 1
    while l < r and signal[l] != start:
        l += 1
    r = l + 1
print(max_length)
