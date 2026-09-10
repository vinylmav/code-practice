nums = [4, 4, 4, 1, 1, 2, 2, 2, 3]
k = 2
vault = {}
for num in nums:
    vault[num] = vault.get(num, 0) + 1
vault_list = sorted(vault.items(), key=lambda x:x[-1], reverse=True)
print([songid for songid, freq in vault[:k]])

# implementing the bucket sort
# useful when you have fixed ranges
result = []
buckets = [[] for _ in range(len(nums)+1)]
for songid, freq in vault.items():
    buckets[freq].append(songid)
for i in range(len(buckets)-1, 0, -1):
    for num in buckets[i]:
        result.append(num)
        if len(result) == k:
            break
    if len(result) == k:
        break
