class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        n = len(heights)
        
        stack = []
        max_area = float("-inf")

        for idx, height in enumerate(heights):
            start = idx

            while stack and stack[-1][1] > height:
                i, h = stack.pop()
                max_area = max(max_area, (idx-i)*h)
                start = i   
            stack.append((start, height))
        while stack:
            i, h = stack.pop()
            max_area = max(max_area, (n - i)*h)
            start = i            



        return max_area



        