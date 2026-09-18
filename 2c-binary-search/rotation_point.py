nums = [6, 7, 1, 2, 3, 4, 5]
# nums = [3, 4, 5, 6, 7, 1, 2]
# nums = [5, 6, 7, 1, 2, 3, 4]
nums = [1, 2, 3, 4, 5, 6]
# l lowest r (l > r)
def rotation_point(nums):
    n = len(nums)
    lo, hi = 0, n - 1
    while lo < hi:
        mi = (lo + hi) // 2
        if nums[mi] >= nums[lo] and nums[mi] > nums[hi]:
            lo = mi + 1
        else:
            hi = mi
    return lo

print(rotation_point(nums))
