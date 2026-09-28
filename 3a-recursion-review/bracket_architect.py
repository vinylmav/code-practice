n = 1

# n = 2 → ["(())", "()()"]

# n = 3 → ["((()))", "(()())", "(())()", "()(())", "()()()"]

def generate_architect(n, o, c, string, result):
    if o == c == n:
        result.append(string)
        return
    if c > o or o > n:
        return
    generate_architect(n, o + 1, c, string + "(", result)
    generate_architect(n, o, c + 1, string + ")", result)
    return result

print(generate_architect(3, 0, 0, "", []))
