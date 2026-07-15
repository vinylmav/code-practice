import bisect

def binary_search(lst, x):
    idx = bisect.bisect_left(lst, x)
    return idx < len(lst) and lst[idx] == x

# the return statement: bisect_left() gives the index where the element should
# come if it doesnt exist. so we need to check first where the index is possible
# then we check if the element exists at all in the list.
# bisect_left(lst, x) gives the index of the first element that is >= x
