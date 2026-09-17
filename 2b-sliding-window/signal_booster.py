# 1. VALIDITY:  What condition makes window [l, r] valid?
# A: all same characters + boosts >= 0
# 2. TYPE:      Fixed-size or variable-size? (Is window size given/derivable,
# or am I optimizing it?)
# A: variable
# 3. TEMPLATE:
#    - What state do I track? (sum? freq map? count? max_freq?)
# A: max_freq
#    - Expand: what changes when r moves right?
# A: i absorb r, maybe the sequence becomes invalid
#    - Contract: what changes when l moves right?
# A: update the max freq and update the booster formula
#    - Answer: when/how do I update the answer?
# A: when the window is a valid one, you update the answer.
signal = "AAAAAABC"
k = 1
n = len(signal)
max_length = 0
signal_freq = {}
max_freq = 0
l = 0
boosts_used = 0
for r in range(n):
    sig = signal[r]
    signal_freq[sig] = signal_freq.get(sig, 0) + 1
    max_freq = max(max_freq, signal_freq[sig])
    boosts_used = (r - l + 1) - max_freq
    while l < r and boosts_used > k:
        l += 1
        signal_freq[signal[l - 1]] -= 1
        boosts_used = (r - l + 1) - max_freq
    max_length = max(max_length, (r - l + 1))
print(max_length)
