piles = [30, 11, 23, 4, 20]
h = 5
# using BS find which k will satisfy
def predicate(piles, h, k):
    hours = 0
    for pile in piles:
        hours += (pile + k - 1) // k
    return hours <= h

def banana_feast(piles, h):
    lo = 1
    hi = max(piles)
    while lo < hi:
        mi = (lo + hi) // 2
        if predicate(piles, h, mi):
            hi = mi
        else:
            lo = mi + 1
    return lo

print(banana_feast(piles, h))

### math.ceil(a / b) => (a + b - 1) // b
