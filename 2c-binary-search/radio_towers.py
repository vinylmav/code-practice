positions = [1, 2, 4, 8, 9]
m = 3

def predicate(positions, m, spacing):
    n = len(positions)
    count = 1
    l = 0
    for r in range(1, n):
        lrt, rrt = positions[l], positions[r]
        if rrt - lrt >= spacing:
            count += 1
            l = r
    return count >= m

def radio_towers(positions, m):
    positions.sort()
    lo = 0
    hi = positions[-1] - positions[0]
    while lo < hi:
        mi = (lo + hi + 1) // 2
        if predicate(positions, m, mi):
            lo = mi
        else:
            hi = mi - 1
    return lo

print(radio_towers(positions, m))
