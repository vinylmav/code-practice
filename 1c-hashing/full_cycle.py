# S[r] - n*k = S[l-1]
# range of n?
# 0 <= n <= S[r]//k
# which n do i choose?

nums = [23,  2,  6,  4,  7]
k = 13
# maybe the question that i am asking is wrong.
vault = {0: -1}
ps = 0
# store the index of the first occurrence, not a count.
valid = False
for i, num in enumerate(nums):
    ps += num
    if ps % k in vault:
        if i - vault[ps % k] >= 2: # take care of the sign flip
            valid = True
            break
    vault[ps % k] = vault.get(ps % k, i)
print(valid)
