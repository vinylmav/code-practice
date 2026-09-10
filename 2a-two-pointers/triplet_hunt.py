nums = [-1, 0, 1, 2, -1, -4]
nums.sort()
n = len(nums)
result = []
for i in range(n):
    # although this is kinda intentional - i used the python indexing shortcut.
    # for the first iteration 0 and n-1 index will be compared, but still that's fine.
    # anyways the industry standard is to use the following.
    if i > 0 and nums[i] == nums[i - 1]:
        continue
    a = nums[i]
    l, r = i + 1, n - 1
    while l < r:
        b, c = nums[l], nums[r]
        if (b + c) < -a:
            l += 1
        elif (b + c) > -a:
            r -= 1
        else:
            result.append([a, b, c])
            l += 1
            r -= 1
            # the new b and c values might be duplicates. cross them all.
            while l < r and nums[l] == nums[l - 1]:
                l += 1
            while l < r and nums[r] == nums[r + 1]:
                r -= 1
print(result)
