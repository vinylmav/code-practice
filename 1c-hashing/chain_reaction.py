nums = [1, 0, -1, -2]
vault = dict.fromkeys(nums, 1)
for num in nums:
    i = num + 1
    while i in vault and vault[i] > 0:
        if vault[i] == 1:
            vault[i] *= -1
            vault[num] += 1
            i += 1
        elif vault[i] > 1:
            vault[num] += vault[i]
            break
# find maximum length of consecutive numbers
max_length = max([chain_length for atomic_no, chain_length in vault.items()])
print(max_length)

