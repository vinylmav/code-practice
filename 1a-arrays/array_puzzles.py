def reverse(arr):
    n = len(arr)
    for i in range(n//2):
        arr[i], arr[n-1-i] = arr[n-1-i], arr[i]
    return arr
# print(reverse([1]))

def the_carousel(arr, k):
    n = len(arr)
    k = k % n
    for i in range(k//2):
        arr[i], arr[k-1-i] = arr[k-1-i], arr[i]
    r = n - k
    for i in range(r//2):
        arr[k+i], arr[k+r-1-i] = arr[k+r-1-i], arr[k+i]
    return reverse(arr)

def missing_roll_call(arr):
    n = len(arr)
    actual_total = n * (n+1) // 2
    total = sum(arr)
    return actual_total - total

def ghost_attendance(arr):
    for i in range(len(arr)):
        if arr[abs(arr[i])-1] < 0:
            continue
        arr[abs(arr[i])-1] = -arr[abs(arr[i])-1]
    ans = []
    for i, num in enumerate(arr):
        if num > 0:
            ans.append(i+1)
    return ans

# def cleanup_crew(arr):
#     n = len(arr)
#     i = 0
#     j = 0
#     found_zero = False
#     while j < n:
#         if found_zero:
#             arr[i], arr[j] = arr[j], arr[i]
#         if arr[i] == 0:
#             found_zero = True
#         else:
#             i += 1
#         j += 1
#     return arr

# there is even a better way to write this off
def cleanup_crew(arr):
    write = 0
    for read, value in enumerate(arr):
        if value != 0:
            arr[read], arr[write] = arr[write], arr[read]
            write += 1
    return arr

print(cleanup_crew([1, 2, 3]))
