def merge_sort(arr):
    if len(arr) <= 1:
        return (arr, 0)
    sep = len(arr)//2
    left_branch, left_inv = merge_sort(arr[:sep])
    right_branch, right_inv = merge_sort(arr[sep:])
    sorted_arr = []
    cross_inv = 0
    i = j = 0
    while i < len(left_branch) and j < len(right_branch):
        if right_branch[j] >= left_branch[i]:
            sorted_arr.append(left_branch[i])
            i += 1
        else:
            cross_inv += len(left_branch[i:])
            sorted_arr.append(right_branch[j])
            j += 1
    sorted_arr.extend(left_branch[i:])
    sorted_arr.extend(right_branch[j:])
    total_inversions = left_inv + right_inv + cross_inv
    return (sorted_arr, total_inversions)

print(merge_sort([2, 4, 1, 3, 5]))
