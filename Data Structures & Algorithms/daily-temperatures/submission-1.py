class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        n = len(temperatures)
        
        result = [0]*n
        stack = []

        i = 0
        while i < n:

            while stack and temperatures[stack[-1]] <= temperatures[i]:
                idx = stack.pop()
                result[idx] = (i - idx)
            stack.append(i)
            i += 1
        return result







        