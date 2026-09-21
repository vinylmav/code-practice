bloom_days = [7, 7, 7, 7, 12, 7, 7]
m = 2
k = 3

def predicate(bloom_days, m, k, days):
    n = len(bloom_days)
    l = 0
    valid = 0
    bouquets_made = 0
    for r in range(n):
        if bloom_days[r] <= days:
            valid += 1
        if r - l + 1 == k:
            if valid == k:
                bouquets_made += 1
                valid = 0
                l = r + 1
            else:
                if bloom_days[l] <= days:
                    valid -= 1
                l += 1
    return bouquets_made >= m

def flower_festival(bloom_days: list[int], m, k):
    n = len(bloom_days)
    if n < m * k:
        return -1
    lo, hi = min(bloom_days), max(bloom_days)
    while lo < hi:
        mi = (lo + hi) // 2
        if predicate(bloom_days, m, k, mi):
            hi = mi
        else:
            lo = mi + 1
    return lo

print(flower_festival(bloom_days, m, k))