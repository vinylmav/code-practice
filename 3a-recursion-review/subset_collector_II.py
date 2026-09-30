nums = [1, 2, 2, 3]
nums.sort()

def subset_collector_ii(nums, index, subset, result):
    if index == len(nums):
        result.append(subset[:])
        return
    subset.append(nums[index])
    subset_collector_ii(nums, index + 1, subset, result)
    subset.pop()
    next_index = index + 1
    while next_index < len(nums) and nums[index] == nums[next_index]:
        next_index += 1
    subset_collector_ii(nums, next_index, subset, result)
    return result

print(subset_collector_ii(nums, 0, [], []))
