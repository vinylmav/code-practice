n = 4
k = 2

def combination_lock(n, k, num, combination, result):
    if num > n + 1:
        return
    if len(combination) == k:
        result.append(combination[:])
        return
    combination.append(num)
    combination_lock(n, k, num + 1, combination, result)
    combination.pop()
    combination_lock(n, k, num + 1, combination, result)
    return result

print(combination_lock(n, k, 1, [], []))
