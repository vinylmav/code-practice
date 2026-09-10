# Input:  ["a", "a", "b", "b", "c", "c", "c"]
# Output: 6, chars = ["a", "2", "b", "2", "c", "3"]

# Input:  ["a"]
# Output: 1, chars = ["a"]

# Input:  ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
# Output: 4, chars = ["a", "b", "1", "2"]
#                (b appears 12 times → "12" → two chars "1","2")
# Constraints: 1 ≤ n ≤ 2000
chars = ["a", "a", "a", "b", "b", "c", "c", "c", "c", "d", "d"]
n = len(chars)
r, w = 1, 0
count = 1  # 3
while r < n:
    if chars[r] != chars[r - 1]:
        chars[w] = chars[r - 1]
        w += 1
        if count >= 2:
            for num in str(count):
                chars[w] = num
                w += 1
        count = 1
    else:
        count += 1
    r += 1
chars[w] = chars[r - 1]
w += 1
if count >= 2:
    for num in str(count):
        chars[w] = num
        w += 1
print(w, chars[:w])
