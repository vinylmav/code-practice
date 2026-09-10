def overbooked_calendar(reservations):
    reservations.sort(key= lambda x: x[-1])
    result = 0
    prev_end = reservations[0][1]
    for curr_start, curr_end in reservations[1:]:
        if prev_end > curr_start:
            result += 1
        else:
            prev_end = curr_end
    return result

print(overbooked_calendar([[1,4], [2,3], [3,5]]))
