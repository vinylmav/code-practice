# 1. VALIDITY:  What condition makes window [l, r] valid?
# A: if it contains all the ch in pattern string
# 2. TYPE:      Fixed-size or variable-size? (Is window size given/derivable,
# or am I optimizing it?)
# A: fixed
# 3. TEMPLATE:
#    - What state do I track? (sum? freq map? count? max_freq?)
# A: freq map
#    - Expand: what changes when r moves right?
# A: add the new ch to the map and change seen
#    - Contract: what changes when l moves right?
# A: sub the ch from the map and change seen
#    - Answer: when/how do I update the answer?
# A: if valid window is found break
pattern = "abc"
text = "aabcidbaooo"
def permutation_scanner(pattern, text):
    n = len(text)
    pattern_map = {}
    need = len(pattern)
    for i in range(need):
        ch = pattern[i]
        pattern_map[ch] = pattern_map.get(ch, 0) + 1
    text_map = {}
    l = 0
    seen = 0
    for r in range(need):
        ch = text[r]
        text_map[ch] = text_map.get(ch, 0) + 1
        if ch in pattern_map and text_map[ch] <= pattern_map[ch]:
            seen += 1
    if seen == need:
        return True
    k = need
    for r in range(k, n):
        l_ch = text[l]
        if l_ch in pattern_map and text_map[l_ch] <= pattern_map[l_ch]:
            seen -= 1
        text_map[l_ch] = text_map.get(l_ch, 0) - 1
        r_ch = text[r]
        text_map[r_ch] = text_map.get(r_ch, 0) + 1
        if r_ch in pattern_map and text_map[r_ch] <= pattern_map[r_ch]:
            seen += 1
        if seen == need:
            return True
        l += 1
    return False

print(permutation_scanner(pattern, text))
