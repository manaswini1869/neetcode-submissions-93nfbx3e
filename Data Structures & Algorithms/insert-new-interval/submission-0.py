class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key=lambda x: x[0])

        i = 0
        while intervals and i < len(intervals)-1:
            if intervals[i][1] >= intervals[i+1][0]: 
                intervals[i][1] = max(intervals[i][1], intervals[i+1][1])
                del intervals[i+1]
            else:
                i += 1 


        # new_start = newInterval[0]
        # new_end = newInterval[1]

        # for start, end in intervals:


        return intervals

