nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
n = len(nums)
k = 1
r, w = 1, 1
while r < n:
    if nums[r] != nums[w - 1]:
        nums[w] = nums[r]
        w += 1
        k += 1
    r += 1
print(k, nums)
