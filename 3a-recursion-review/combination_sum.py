candidates = [2, 3, 5]
target = 8

def combination_sum(candidates, target, m, candidate, total, result):
    if total > target:
        return
    if total == target:
        result.append(candidate[:]) # snapshot
        return
    for i in range(m, len(candidates)):
        c = candidates[i]
        total += c
        candidate.append(c)
        combination_sum(candidates, target, i, candidate, total, result)
        candidate.pop()
        total -= c
    return result

print(combination_sum(candidates, target, 0, [], 0, []))
