from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # Get first item of each tuples sorted
        intervals.sort()
        for i in range(len(intervals)-1):
            # Return False if the following meeting starts before
            # the previous meeting ends
            if intervals[i][1] > intervals[i+1][0]:
                return False
        return True


intervals = [[0,30],[5,10],[15,20]] # False
#intervals = [[7,10],[2,4]] # True
print(Solution().canAttendMeetings(intervals))
