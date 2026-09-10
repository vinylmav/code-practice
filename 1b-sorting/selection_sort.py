def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min_value = arr[i]
        min_index = i
        for j in range(i+1, n):
            if arr[j] < min_value:
                min_index = j
                min_value = arr[j]
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

print(selection_sort([3, 5, 1, 4, 2]))
