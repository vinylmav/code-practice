weights = [1, 2, 3, 1, 1]
days = 4

def predicate(weights, days, capacity):
    days_required = 0
    shipment = 0
    i = 0
    n = len(weights)
    while i < n:
        weight = weights[i]
        shipment += weight
        if shipment > capacity:
            days_required += 1
            shipment = 0
        else:
            i += 1
    if shipment > 0:
        days_required += 1
    return days_required <= days

def cargo_ship(weights, days):
    lo = max(weights)
    hi = sum(weights)
    while lo < hi:
        mi = (lo + hi) // 2
        if predicate(weights, days, mi):
            hi = mi
        else:
            lo = mi + 1
    return lo

print(cargo_ship(weights, days))
