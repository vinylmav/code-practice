def power(base, exp):
    if exp == 0:
        return 1
    return base * power(base, exp - 1)

def fast_power(base, exp):
    if exp == 0:
        return 1
    if exp % 2 == 0:
        exp = exp//2
        a = fast_power(base, exp)
        return a * a
    else:
        exp = exp//2
        a = fast_power(base, exp)
        return a * a * base

print(fast_power(2, 20))
