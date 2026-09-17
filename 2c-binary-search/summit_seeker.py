nums = [1, 2, 1, 3, 4, 5, 6, 7]

def summit_seeker(nums):
    n = len(nums)
    lo, hi = 0, n - 1
    if n == 1:
        return 0
    if n == 2:
        return 0 if nums[0] > nums[1] else 1
    while lo < hi:
        mi = (lo + hi) // 2
        if nums[mi - 1] > nums[mi] > nums[mi + 1]:
            hi = mi - 1
        elif nums[mi - 1] < nums[mi] > nums[mi + 1]:
            return mi
        else:
            lo = mi + 1
    return lo

print(summit_seeker(nums))
