nums = [1, 2, 3]
used_map = {}
for num in nums:
    used_map[num] = False

def arrangement_game(nums, used_map, permutation, result):
    if len(permutation) == len(nums):
        result.append(permutation[:])
        return
    for num in nums:
        if not used_map[num]:
            used_map[num] = True
            permutation.append(num)
            arrangement_game(nums, used_map, permutation, result)
            permutation.pop()
            used_map[num] = False
    return result

print(arrangement_game(nums, used_map, [], []))
