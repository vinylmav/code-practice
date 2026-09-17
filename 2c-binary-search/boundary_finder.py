nums = [5, 7, 7, 8, 8, 10]
target = 6

def first_true(nums, target):
    n = len(nums)
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

def last_true(nums, target):
    n = len(nums)
    if n == 0:
        return -1
    lo, hi = 0, n - 1
    while lo < hi:
        mi = (lo + hi + 1) // 2
        if nums[mi] <= target:
            lo = mi
        else:
            hi = mi - 1
    return lo if nums[lo] == target else -1

def boundary_finder(nums, target):
    return [first_true(nums, target), last_true(nums, target)]

print(boundary_finder(nums, target))
