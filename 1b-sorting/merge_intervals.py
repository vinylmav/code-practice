def merge_intervals(schedule):
    """Merge all overlapping meetings into the fewest non-overlapping blocks"""
    schedule.sort(key= lambda x: x[0])
    merged_intervals = []
    merged_intervals.append(schedule[0])
    for curr_start, curr_end in schedule[1:]:
        prev_start = merged_intervals[-1][0]
        prev_end = merged_intervals[-1][1]
        if curr_start <= prev_end:
            merged_intervals[-1][0] = prev_start
            merged_intervals[-1][1] = max(prev_end, curr_end)
        else:
            merged_intervals.append([curr_start, curr_end])
    return merged_intervals

arr = [[1,4], [0,1], [3,5], [2,3]]
print(merge_intervals(arr))
