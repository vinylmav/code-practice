# arr = [2, 7, 11, 15]
arr = [3, 2, 3, 4]
target = 6
# complement search
vault = {}
for i, num in enumerate(arr):
    # check and then store
    if target - num in vault:
        print([vault[target - num], i])
    vault[num] = i
