def subsets(arr, subsets_arr=None):
    if subsets_arr is None:
        subsets_arr = []
    if len(arr) == 0:
        print(subsets_arr)
        return
    subsets(arr[1:], subsets_arr + [arr[0]])
    subsets(arr[1:], subsets_arr)

subsets([1, 2, 3])
