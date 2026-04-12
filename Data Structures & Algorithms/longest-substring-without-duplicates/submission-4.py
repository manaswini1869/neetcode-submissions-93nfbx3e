class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        ans = float("-inf")
        n = len(s)
        if n < 2:
            return n 
        left, right = 0, 1
        seen = set(s[left])
        while right < n:
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            ans = max(ans, right - left + 1)
            right += 1
        return ans




        