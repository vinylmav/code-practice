height = [4, 3, 2, 1, 4]
n = len(height)
l, r = 0, n - 1
max_area = 0
while l <= r:
    area = min(height[l], height[r]) * (r - l)
    # max_area = area if area > max_area else max_area
    # pythonic way below
    max_area = max(max_area, area)
    if height[l] < height[r]:
        l += 1
    else:
        r -= 1
print(max_area)
