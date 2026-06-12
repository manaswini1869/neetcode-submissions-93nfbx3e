class Solution:
    def trap(self, height: List[int]) -> int:

        res = 0

        n = len(height)

        prefix = [-1]*n
        suffix = [-1]*n
        suffix[-1] = height[-1]
        for i in range(n):
            prefix[i] = max(prefix[i-1], height[i])
        for j in range(n-2, -1, -1):
            suffix[j] = max(suffix[j+1], height[j])
        print(prefix, suffix)
        for i in range(n):
            res += min(prefix[i], suffix[i]) - height[i]
        return res

        