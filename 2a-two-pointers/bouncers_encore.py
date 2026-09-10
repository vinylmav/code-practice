nums = [0, 0, 0, 0, 0, 1, 1, 1, 2, 3, 3]
n = len(nums)
r, w = 1, 1
d = 1
# tracking with a d state is unnecessary.
# given the array is sorted if nums[r] == nums[w - 2], then:
# nums[r] == nums[w - 1], so taking in nums[r] would be too much.
# this is the predicate.
# while r < n:
#     if nums[r] != nums[w - 1]:
#         nums[w] = nums[r]
#         w += 1
#         d = 1
#     else:
#         d += 1
#         if d == 2:
#             nums[w] = nums[r]
#             w += 1
#     r += 1
# the straight forward approach is:
while (r < n):
    if nums[r] != nums[w - 2]:
        nums[w] = nums[r]
        w += 1
    r += 1
print(nums)
