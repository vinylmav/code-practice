# 1. VALIDITY:  What condition makes window [l, r] valid?
# A: it should be of length k
# 2. TYPE:      Fixed-size or variable-size? (Is window size given/derivable,
# or am I optimizing it?)
# A: fixed size, looking for the maximum score in a window
# 3. TEMPLATE:
#    - What state do I track? (sum? freq map? count? max_freq?)
# A: the maximum score
#    - Expand: what changes when r moves right?
# A: that score from the sum gets subtracted
#    - Contract: what changes when l moves right?
# A: that score will be added to the sum
#    - Answer: when/how do I update the answer?
# when i find a score greater than the saved maximum.
scores = [1, 1, 1, 1, 1]
k = 5
n = len(scores)
# calculate the first window
max_score = 0
window_sum = 0
for r in range(k):
    window_sum += scores[r]
max_score = max(max_score, window_sum)
l = 0
for r in range(k, n):
    # add the current element, remove the element at l.
    window_sum = window_sum - scores[l] + scores[r]
    # update the maximum score
    max_score = max(max_score, window_sum)
    l += 1
print(max_score)
