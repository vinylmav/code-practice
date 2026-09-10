def partition(arr, low, high):
    pivot_index = high
    boundary = low
    for i in range(low, high+1):
        if arr[i] < arr[pivot_index]:
            arr[i], arr[boundary] = arr[boundary], arr[i]
            boundary += 1
    arr[boundary], arr[pivot_index] = arr[pivot_index], arr[boundary]
    pivot_index = boundary
    return pivot_index

def quicksort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quicksort(arr, low, pivot_index - 1)
        quicksort(arr, pivot_index + 1, high)

arr = [7, 6, 5, 4, 3, 2, 1]
n = len(arr)
quicksort(arr, 0, n - 1)
print(arr)
