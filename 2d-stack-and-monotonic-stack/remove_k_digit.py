num = "33526221184202197273"
k = 19
def remove_k_digits(num, k):
    if len(num) == k:
        return '0'
    stack = []
    n = len(num)
    print(n)
    removed = 0
    for i in range(n):
        while removed < k and stack and stack[-1] > num[i]:
            stack.pop()
            removed += 1
        stack.append(num[i])
        print(stack)
    print(k, removed)
    return ''.join(stack[:len(stack) if k == removed else len(stack) - (k - removed)]).lstrip('0') or '0'
print(remove_k_digits(num, k))
