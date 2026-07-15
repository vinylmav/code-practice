def palindrome(string):
    if len(string) == 0:
        return True
    if string[0].lower() == string[-1].lower():
        return palindrome(string[1:-1])
    else:
        return False

print(palindrome("racecar"))