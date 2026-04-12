class Solution:
    def maxArea(self, heights: List[int]) -> int:

        n = len(heights)
        left, right = 0, n-1
        ans = float("-inf")

        while left < right:
            ans = max(ans, min(heights[left], heights[right])*(right-left))
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return ans



        