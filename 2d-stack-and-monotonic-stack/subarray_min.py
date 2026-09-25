arr = [3, 1, 2, 4]
arr = [11, 81, 94, 43, 3]
arr = [2, 5, 2]
arr = [2,4,3,3,5,4,9,6]
arr = [3,5,2,6]
arr = [5,4,3,2,1]
n = len(arr)
nse_stack = []
pse_stack = []
nse_result = [n] * n
pse_result = [-1] * n
for i in range(n):
    while nse_stack and arr[nse_stack[-1]] > arr[i]:
       nse_result[nse_stack.pop()] = i
    nse_stack.append(i)
    while pse_stack and arr[pse_stack[-1]] > arr[i]:
        pse_stack.pop()
    pse_result[i] = pse_stack[-1] if pse_stack else -1
    pse_stack.append(i)
print(nse_result, pse_result)
result = 0
for i in range(n):
    l_win, r_win = i - pse_result[i], nse_result[i] - i
    result = (result + l_win * r_win * arr[i]) % (10**9 + 7)
print(result)
