# bullshit attempts
height = [4, 2, 0, 3, 2, 5]
n = len(height)
left_maximum = [0]*n
right_maximum = [0]*n
lm, rm = -1, -1
for i in range(n):
    if height[i] > lm:
        lm = height[i]
    if height[n - 1 - i] > rm:
        rm = height[n - 1 - i]
    left_maximum[i] = lm
    right_maximum[n - 1 - i] = rm
water_collected = 0
for i, h in enumerate(height[1:-1]):
    water_collected += max(0, min(left_maximum[i], right_maximum[i+2]) - h)
# print(water_collected)
# the above solution is valid but we use O(n) space. can be solved without extra space!
# the optimized O(n) solution with O(1) extra space. below!
height = [4, 2, 0, 3, 2, 5]
ml, mr = height[0], height[n - 1]
l, r = 1, n - 2
water_collected = 0
while l <= r:
    if ml < mr:
        water_collected += max(ml - height[l], 0)
        ml = max(height[l], ml)
        print(l, water_collected)
        l += 1
    else:
        water_collected += max(mr - height[r], 0)
        mr = max(height[r], mr)
        print(r, water_collected)
        r -= 1
print(water_collected)
