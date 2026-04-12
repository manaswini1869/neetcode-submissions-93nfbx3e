class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        n = len(queries)
        res = [-1]*n

        for i in range(n):
            val = float("inf")
            for start, end in intervals:
                if start <= queries[i] <= end:
                    val = min(val, end - start + 1)
            if val != float("inf"):
                res[i] = val

        return res
            

            
