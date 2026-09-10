nums = [1, -1, 1, 1, -1]
#    = [0, 1, 0, 1, 2, 1]
k = 1
ps = 0
# S[r] - S[l-1] = k
vault = {0: 1}
total_count = 0
for s in nums:
    ps += s
    if ps - k in vault:
        total_count += vault[ps - k]
    vault[ps] = vault.get(ps, 0) + 1
print(total_count)
