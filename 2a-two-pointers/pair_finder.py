nums = [1, 3, 4, 5, 7, 10, 11]
t = 9
def pair_finder(nums, t):
    n = len(nums)
    l, r = 0, n-1
    while l < r:
        if nums[l] + nums[r] < t:
            l += 1
        elif nums[l] + nums[r] > t:
            r -= 1
        else:
            return (l, r)
    return -1
print(pair_finder(nums, t))
