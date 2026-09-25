nums = [3, 1, 4, 2, 5]
stack = [0]
# NSE
# stack => monotonously increasing from bottom to up
# pop condition: when incoming is less then stack top
ans = [-1] * len(nums)
for i in range(1, len(nums)):
    while stack and nums[i] < nums[stack[-1]]:
        ans[stack.pop()] = nums[i]
    stack.append (i)
print("NSE", ans)

# NGE
# stack => monotonously decreasing from bottom to top
# pop => when incoming is more than stack top
ans = [-1] * len(nums)
stack = [0]
for i in range(1, len(nums)):
    while stack and nums[stack[-1]] < nums[i]:
        ans[stack.pop()] = nums[i]
    stack.append(i)
print("NGE", ans)

# PGE
#
#
nums = [5, 4, 2, 1, 4, 2, 5]
ans = [-1] * len(nums)
stack = [0]
for i in range(1, len(nums)):
    if nums[stack[-1]] < nums[i]:
        stack.pop()
        stack.append(i)
    else:
        ans[i] = nums[stack[-1]]
print("PGE", ans)

# PSE
nums = [1, 2, 3, 4, 5]
stack = [0]
n = len(nums)
ans = [-1] * n
for i in range(1, n):
    while stack and nums[stack[-1]] >= nums[i]:
        stack.pop()
    if stack:
        ans[i] = nums[stack[-1]]
    stack.append(i)
print(ans)

nums = [5, 5, 4, 1]
stack = [0]
n = len(nums)
ans = [-1] * n
for i in range(n):
    while stack and nums[stack[-1]] <= nums[i]:
        stack.pop()
    if stack:
        ans[i] = nums[stack[-1]]
    stack.append(i)
print(ans)
