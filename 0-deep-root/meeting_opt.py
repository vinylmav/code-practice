# Given a list of intervals [[start, end], ...], find the minimum number of meeting
# rooms required to hold all meetings simultaneously without conflict.

# Example:
#     intervals = [[0,30],[5,10],[15,20]]
#     Output: 2

def optimise_meetings(meetings):
    import heapq
    meetings.sort(key=lambda x: x[0])
    heap = []
    for meeting in meetings:
        if heap and heap[0] <= meeting[0]:
            heapq.heappop(heap)

        heapq.heappush(heap, meeting[1])

    return len(heap)

intervals = [[0,30],[5,10],[15,20]]
print(optimise_meetings(intervals))

def min_meeting_rooms(intervals):
    """
        Returns the minimum number of meeting rooms
        required to organise the meetings with the
        given intervals.
    """
    import heapq
    # first we sort the meetings using the start time.
    intervals.sort(key=lambda x: x[0])
    heap = []

    for meeting in intervals:
        if heap and heap[0] <= meeting[0]:
            heapq.heappop(heap)
        heapq.heappush(heap, meeting[1])

    return len(heap)
