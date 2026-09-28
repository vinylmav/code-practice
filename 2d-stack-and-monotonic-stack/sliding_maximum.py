from collections import deque

nums = [1,3,-1,-3,5,3,6,7]
k = 3

def sliding_maximum(nums, k):
    n = len(nums)
    dq = deque()
    result = []
    for i in range(n):
        # 1. evict from the back
        while dq and nums[dq[-1]] <= nums[i]:
            dq.pop()
        # 2. append
        dq.append(i)
        # 3. evict from the front
        if dq[0] <= i - k:
            dq.popleft()
        # 4. record if your window is full
        if i + 1 >= k:
            result.append(nums[dq[0]])
    return result

print(sliding_maximum(nums, k))
