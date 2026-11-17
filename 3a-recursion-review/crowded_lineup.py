nums = [2, 2, 2]
nums.sort()
used_map = {}
freq_map = {}
for num in nums:
    used_map[num] = 0
    freq_map[num] = freq_map.get(num, 0) + 1

def crowded_lineup(nums, permutation, result):
    if len(permutation) == len(nums):
        result.append(permutation[:])
        return
    i = 0
    while i < len(nums):
        num = nums[i]
        if used_map[num] < freq_map[num]:
            used_map[num] += 1
            permutation.append(num)
            crowded_lineup(nums, permutation, result)
            permutation.pop()
            used_map[num] -= 1
        i += 1
        while i < len(nums) and nums[i] == nums[i - 1]:
            i += 1
    return result

print(crowded_lineup(nums, [], []))
