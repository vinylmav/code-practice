nums = [1, 2, 3]

def subset_collector(nums, index, subset, result):
    if index == len(nums):
        result.append(subset)
        return
    subset_collector(nums, index + 1, subset + [nums[index]], result)
    subset_collector(nums, index + 1, subset, result)
    return result

print(subset_collector(nums, 0, [], []))
