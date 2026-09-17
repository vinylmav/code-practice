colors = [1, 2, 1, 2, 3]
k = 2
def mosaic_strip(colors, k):
    n = len(colors)
    count = 0
    seen = 0
    colors_map = {}
    l = 0
    for r in range(n):
        c = colors[r]
        colors_map[c] = colors_map.get(c, 0) + 1
        if colors_map[c] == 1:
            seen += 1
        while l <= r and seen > k:
            lc = colors[l]
            colors_map[lc] -= 1
            if colors_map[lc] == 0:
                seen -= 1
            l += 1
        count += (r - l + 1)
    return count
print(mosaic_strip(colors, k) - mosaic_strip(colors, k-1))

# exactly k = atmost(k) - atmost(k-1)
