# simple problem
# since the sequence is sorted, look at both the ends.
# pick the number that is largest and then move on.
nums = [-7, -3, 2, 3, 11]
n = len(nums)
l, r = 0, n - 1
squares = [0]*n
i = n - 1
while l <= r:
    left, right = abs(nums[l]), abs(nums[r])
    if left > right:
        squares[i] = left**2
        l += 1
    else:
        squares[i] = right**2
        r -= 1
    i -= 1
print(squares)
