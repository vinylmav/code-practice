nums1 = [1, 2]
nums2 = [-2, -1]
nums3 = [-1, 2]
nums4 = [0, 2]
# n1 + n2 = (-n3 + -n4)
# first find a sum of two numbers.
possible_sums = {}
for i in range(len(nums1)):
    for j in range(len(nums2)):
        num1 = nums1[i] + nums2[j]
        possible_sums.setdefault(num1, []).append((i, j))
# given this number, think whether you can find a fitting number from the other two.
for k in range(len(nums3)):
    for l in range(len(nums4)):
        num2 = -(nums3[k] + nums4[l])
        if num2 in possible_sums:
            for pair in possible_sums[num2]:
                print(pair[0], pair[1], k, l)
# all we have to check now is whether thers is num2 in the vault
