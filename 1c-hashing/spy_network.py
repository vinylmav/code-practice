strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
vault = {}
for string in strs:
    sorted_string = ''.join(sorted(string))
    # vault[sorted_string] = vault.get(sorted_string, []) + [string]
    # better way is the one below
    vault.setdefault(sorted_string, []).append(string)
# result = [value for key, value in vault.items()]
# better way exists
result = list(vault.values())
print(result)
