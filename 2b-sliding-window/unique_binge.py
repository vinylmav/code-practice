s = "pwwpkew"
n = len(s)
l, r = 0, 0
vault = {}
max_stretch = 0
while r < n:
    if s[r] in vault:
        l = max(vault[s[r]] + 1, l)
    vault[s[r]] = r
    max_stretch = max(max_stretch, r - l + 1)
    print(l, r, vault, r - l + 1)
    r += 1
print(max_stretch)
