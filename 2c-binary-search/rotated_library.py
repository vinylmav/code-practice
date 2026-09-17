nums = [3, 1]
target = 3
# predicate = nums[i] <= nums[i+1]
# after landing on mi, check which side is sorted one.
# if the value belongs in the range of sorted side, do binary search
# else keep searching for such side in [mi, hi]
def binary_search(nums, target, lo, hi):
    while lo < hi:
        mi = (lo + hi) // 2
        if nums[mi] >= target:
            hi = mi
        else:
            lo = mi + 1
    return lo if nums[lo] == target else -1

def rotated_library(nums, target):
    n = len(nums)
    lo, hi = 0, n - 1
    while lo < hi:
        mi = (lo + hi) // 2
        if nums[lo] <= nums[mi]:
            # left side is sorted
            if nums[lo] <= target <= nums[mi]:
                return binary_search(nums, target, lo, mi)
            else:
                lo = mi + 1
        else:
            # right side is sorted
            if nums[mi] <= target <= nums[hi]:
                return binary_search(nums, target, mi, hi)
            else:
                hi = mi - 1
    return lo if nums[lo] == target else -1

print(rotated_library(nums, target))
