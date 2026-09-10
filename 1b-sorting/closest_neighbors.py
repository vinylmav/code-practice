arr = [3, 8, -10, 23, 19, -4, -14, 27]
arr.sort()
md = 10**6 + 1
for i, num in enumerate(arr[:-1]):
    ad = abs(num - arr[i+1])
    # You don't need abs() — after sorting, arr[i+1] - arr[i] is always non-negative.
    if ad < md:
        md = ad
result = []
for i, num in enumerate(arr[:-1]):
    if abs(num - arr[i+1]) == md:
        result.append([num, arr[i+1]])
print(result)
