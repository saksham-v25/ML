class Solution:
    from typing import List 
    def isIntersect(self, intervals):
        intervals.sort()

        start1 = intervals[0][0]
        end1 = intervals[0][1]

        for i in range(1, len(intervals)):
            start2 = intervals[i][0]
            end2 = intervals[i][1]

            if end1 >= start2:
                return True

            end1 = max(end1, end2)

        return False