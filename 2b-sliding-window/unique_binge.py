# 1. VALIDITY:  What condition makes window [l, r] valid?
# A: if all the genres are unique
# 2. TYPE:      Fixed-size or variable-size? (Is window size given/derivable,
# or am I optimizing it?)
# A: variable
# 3. TEMPLATE:
#    - What state do I track? (sum? freq map? count? max_freq?)
# A: i keep a freq map.
#    - Expand: what changes when r moves right?
# A: i add the character to the frequency map
#    - Contract: what changes when l moves right?
# A: we decrease the frequency of the lth ch.
#    - Answer: when/how do I update the answer?
# A: when the window becomes valid again/ when count(s[r]) == 1 again.

s = "abba"
l, r = 0, 0
n = len(s)
count = {}
max_length = 0
for r in range(n):
    # add the r
    count[s[r]] = count.get(s[r], 0) + 1
    # as long as invalid remove the l
    while l < r and count[s[r]] > 1:
        count[s[l]] -= 1
        l += 1
    # update the max_length
    max_length = max(max_length, r - l + 1)
print(max_length)
