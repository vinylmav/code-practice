s = "ADOBECODEBANC"
s = "a"
t = "aa"
n = len(s)
t_map = {}
total_vtm = len(t)
for ch in t:
    t_map[ch] = t_map.get(ch, 0) + 1
l, r = 0, 0
seen = 0
min_stretch = 10**5 + 1
req_substring = ''
subs_map = {}
while r < n:
    print(l, r, seen)
    if s[r] in t_map:
        subs_map[s[r]] = subs_map.get(s[r], 0) + 1
        if subs_map[s[r]] <= t_map[s[r]]:
            seen += 1
    if seen == total_vtm:
        if (r - l + 1) < min_stretch:
            min_stretch = r - l + 1
            req_substring = s[l:r+1]
        if s[l] in t_map:
            subs_map[s[l]] -= 1
            if subs_map[s[l]] < t_map[s[l]]:
                seen -= 1
        if subs_map[s[r]] <= t_map[s[r]]:
            seen -= 1
        subs_map[s[r]] -= 1
        l += 1
    else:
        r += 1
print(req_substring)
