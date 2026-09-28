arr = [3, 1, 2, 4]
arr = [11, 81, 94, 43, 3]

def subarray_minimums_sum(arr):
    n = len(arr)
    mod = 10**9 + 7
    stack = []
    result = 0
    for i in range(n + 1):
        compare = arr[i] if i < n else 0
        while stack and arr[stack[-1]] > compare:
            ni = stack.pop()
            r_win = i - ni
            l_win = ni - (stack[-1] if stack else -1)
            result = (result + r_win * l_win * arr[ni]) % mod
        stack.append(i)
    return result

print(subarray_minimums_sum(arr))
