def reverse_pairs(arr):
    n = len(arr)
    if n <= 1:
        return arr, 0
    left_arr, left_inv = reverse_pairs(arr[:n//2])
    right_arr, right_inv = reverse_pairs(arr[n//2:])
    l_len, r_len = len(left_arr), len(right_arr)
    l, r, curr_inv = 0, 0, 0
    sorted = []
    while l < l_len and r < r_len:
        if left_arr[l] > 2 * right_arr[r]:
            curr_inv += l_len - l
            r += 1
        else:
            l += 1
    r, l = 0, 0
    while l < l_len and r < r_len:
        if left_arr[l] <= right_arr[r]:
            sorted.append(left_arr[l])
            l += 1
        else:
            sorted.append(right_arr[r])
            r += 1
    sorted.extend(left_arr[l:])
    sorted.extend(right_arr[r:])
    return sorted, left_inv + right_inv + curr_inv

sorted_arr, count = reverse_pairs([2, 4, 3, 5, 1])
print(sorted_arr)
print(count)
