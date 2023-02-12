from typing import List


import heapq


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        # Initialize heap
        rooms = []
        # Sort invervals by start time (first item)
        intervals.sort()
        # First meeting requires a room, use end time to indicate
        # when the room gets free -> [0, 30] heap is [30]
        heapq.heappush(rooms, intervals[0][1])

        # Loop through intervals starting at the second item as
        # first room was added
        for item in intervals[1:]:
            # If the room with earliest end time is free
            # use this room. Check by compare with new start time.
            if rooms[0] <= item[0]:
                heapq.heappop(rooms)
            # Add the new end time to the room (got popped earlier)
            # or add a new room
            heapq.heappush(rooms, item[1])
        return len(rooms)


intervals = [[0,30],[5,10],[15,20]] # 2
#intervals = [[7,10],[2,4]] # 1
print(Solution().minMeetingRooms(intervals))
