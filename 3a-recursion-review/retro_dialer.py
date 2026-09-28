phone_map = {
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"]
}

def retro_dialer(number, index, string, result):
    if len(string) == len(number):
        result.append(string)
        return []
    for i in range(len(phone_map[number[index]])):
        retro_dialer(number, index + 1, string + phone_map[number[index]][i], result)
    return result

print(retro_dialer("", 0, "", []))
