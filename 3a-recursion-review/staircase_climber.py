n = 4

cache = {}
def staircase_climber(n):
    if n in cache:
        return cache[n]
    if n == 0:
        return 1
    if n < 0:
        return 0
    cache[n] = staircase_climber(n - 1) + staircase_climber(n - 2)
    return cache[n]

# print(staircase_climber(n))
print(staircase_climber(45))
