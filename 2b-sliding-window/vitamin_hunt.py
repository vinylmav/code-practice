s = "DECFBAA"
t = "ABC"
n = len(s)
# 1. VALIDITY:  What condition makes window [l, r] valid?
# A: it should contain all the vitamins
# 2. TYPE: Fixed-size or variable-size? (Is window size given/derivable,
# or am I optimizing it?)
# A: variable
# 3. TEMPLATE:
#    - What state do I track? (sum? freq map? count? max_freq?)
# A: freq map
#    - Expand: what changes when r moves right?
# A: add the new vitamin to the map and change seen
#    - Contract: what changes when l moves right?
# A: subtract the freq and change the seen accourdingly
#    - Answer: when/how do I update the answer?
# A: keep recording when valid
t_map = {}
need = len(t)
for i in range(need):
    t_map[t[i]] = t_map.get(t[i], 0) + 1
s_map = {}
seen = 0
l = 0
min_length = 10**5 + 1
for r in range(n):
    s_map[s[r]] = s_map.get(s[r], 0) + 1
    if s[r] in t_map and s_map[s[r]] <= t_map[s[r]]:
        seen += 1
    while l <= r and seen == need:
        min_length = min(min_length, r - l + 1)
        if s[l] in t_map and s_map[s[l]] <= t_map[s[l]]:
            seen -= 1
        s_map[s[l]] -= 1
        l += 1
print(min_length)
