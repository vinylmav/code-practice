heights = [2, 4]

# to maximize the area of the largest rectangle for a building,
# find the NSE, PSE for that index.

def npge(heights):
    n = len(heights)
    nse_stack = []
    pse_stack = []
    nse_result = [n] * n
    pse_result = [-1] * n
    for i in range(n):
        while nse_stack and heights[nse_stack[-1]] > heights[i]:
            nse_result[nse_stack.pop()] = i
        nse_stack.append(i)
        while pse_stack and heights[pse_stack[-1]] >= heights[i]:
            pse_stack.pop()
        pse_result[i] = pse_stack[-1] if pse_stack else -1
        pse_stack.append(i)
    return nse_result, pse_result

def architects_view(heights):
    nse, pse = npge(heights)
    n = len(heights)
    max_area = -1
    for i in range(n):
        l = heights[i]
        b = nse[i] - pse[i] - 1
        max_area = max(max_area, l * b)
    return max_area

print(architects_view(heights))


### could be done in a single pass.
def architects_view_improved(heights):
    n = len(heights)
    stack = []
    max_area = 0
    for i in range(n + 1):
        h = heights[i] if i < n else 0
        while stack and heights[stack[-1]] > h:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)
    return max_area
