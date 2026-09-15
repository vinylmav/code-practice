pattern = "ab"
text = "eidbaooo"
n = len(text)
found = False
seen = 0
k = len(pattern)
pattern_vault = {}
text_vault = {}
for ch in pattern:
    pattern_vault[ch] = pattern_vault.get(ch, 0) + 1
# for r in range(n):
#     ch = text[r]
#     if ch in pattern_vault:
#         text_vault[ch] = text_vault.get(ch, 0) + 1
#         if text_vault[ch] <= pattern_vault[ch]:
#             seen += 1
#         if seen == k:
#             found = True
#             break
#     else:
#         seen = 0
# print(found)
# this solution works, but razor is not satisfied.
# use fixed window
for i in range(k):
    ch = text[i]
    if ch in pattern_vault:
        text_vault[ch] = text_vault.get(ch, 0) + 1
        if text_vault[ch] <= pattern_vault[ch]:
                seen += 1
l = 0
for r in range(k, n):
    if seen != k:
        l_ch, r_ch = text[l], text[r]
        if l_ch in pattern_vault:
            if text_vault[l_ch] <= pattern_vault[l_ch]:
                seen -= 1
            text_vault[l_ch] = text_vault.get(l_ch, 0) - 1
        if r_ch in pattern_vault:
            text_vault[r_ch] = text_vault.get(r_ch, 0) + 1
            if text_vault[r_ch] <= pattern_vault[r_ch]:
                seen += 1
        l += 1
    else:
        found = True
        break
if seen == k:
    found = True
print(found)
