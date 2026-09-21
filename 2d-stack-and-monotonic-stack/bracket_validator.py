string = ")("

def bracket_validator(string):
    if len(string) % 2 != 0:
        return False
    stack = []
    match = {
        ")" : "(",
        "}" : "{",
        "]" : "["
    }
    for ch in string:
        if ch in "({[":
            stack.append(ch)
        else:
            if not stack or match[ch] != stack[-1]:
                return False
            stack.pop()
    return len(stack) == 0

print(bracket_validator(string))
