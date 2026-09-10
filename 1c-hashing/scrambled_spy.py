s, t = 'car', 'rat'
s_vault, t_vault = {}, {}
result = True
if len(s) == len(t):
    for i, ch in enumerate(s):
        # better way to do it.
        s_vault[ch] = s_vault.get(ch, 0) + 1
        t_vault[ch] = t_vault.get(ch, 0) + 1
    for i, ch in enumerate(s):
        if not(ch in t_vault and s_vault[ch] == t_vault[ch]):
            result = False
print(result)
