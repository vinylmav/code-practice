nums = [-1, 0, 3, 5, 9, 12]
#       F   F  F  F  T   T   first true
target = 9
def dictionary_lookup(nums, target):
    n = len(nums)
    # predicate: nums[i] >= target
    if n == 0:
        return -1
    lo, hi = 0, n - 1
    while lo < hi:
        mi = (lo + hi) // 2
        if nums[mi] >= target:
            hi = mi
        else:
            lo = mi + 1
    return lo if nums[lo] == target else -1
print(dictionary_lookup(nums, target))
