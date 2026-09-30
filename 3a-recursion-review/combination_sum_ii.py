candidates = [10,1,2,7,6,1,5]
target = 8
candidates.sort()

def combination_sum_ii(candidates, index, total, candidate, target, result):
    if total > target:
        return -1
    if total == target:
        result.append(candidate[:])
        return
    i = index
    while i < len(candidates):
        c = candidates[i]
        candidate.append(c)
        ans = combination_sum_ii(candidates, i + 1, total + c, candidate, target, result)#noqa:E501
        candidate.pop()
        if ans == -1:
            break
        # could also you this:
            # if total + c > target:
                # break
        i += 1
        while i < len(candidates) and candidates[i] == candidates[i - 1]:
            i += 1
    return result

print(combination_sum_ii(candidates, 0, 0, [], target, []))
