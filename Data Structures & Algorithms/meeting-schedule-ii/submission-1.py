"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda x:x.start)
        print(intervals)

        count = 0
        prev_end = intervals[0].end
        for interval in intervals[1:]:
            if prev_end > interval.start:
                count += 1
                prev_end = min(prev_end, interval.end)
            else:
                prev_end = interval.end
        return count+1
        
        
        