def gcd_using_recursion(a, b):
    """
        Returns the highest common factor of a and b.
        Uses recursion.
    """
    if b == 0:
        return a
    return gcd_using_recursion(b, a % b)

def gcd_using_loop(a, b):
    """
        Returns the highest common factor of a and b.
        Uses loops.
    """
    while b != 0:
        a, b = b, a % b
    return a

print(gcd_using_loop(48, 18))
print(gcd_using_recursion(48, 18))
