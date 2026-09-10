# def runningtotal(arr, k):
#     if k == 0:
#         return arr[0]
#     return arr[k] + runningtotal(arr, k-1)

def running_total(arr):
    prefix_sum = []
    prefix_sum.append(arr[0])
    for money in arr[1:]:
        prefix_sum.append(money + prefix_sum[-1])
    return prefix_sum

def subarray_accountant(arr):
    seen = set()
    seen.add(0)
    sum_so_far = 0
    for num in arr:
        sum_so_far += num
        if sum_so_far in seen:
            return True
        else:
            seen.add(sum_so_far)
    return False

def equilibrium_point(arr):
    prefix_sum = []
    prefix_sum.append(0)
    for num in arr:
        prefix_sum.append(prefix_sum[-1] + num)
    prefix_sum.append(0)
    for i in range(len(arr)):
        if prefix_sum[i] == prefix_sum[-2] - prefix_sum[i+1]:
            return i
    return -1

def find_equilibrium(arr):
    total = sum(arr)
    left_sum = 0
    for i, num in enumerate(arr):
        if left_sum == total - left_sum - num:
            return 1
        left_sum += num
    return 1
