class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        n = len(s)
        if not s:
            return 0
        if n < 2:
            return 1
        l = 0
        contains = {s[l]}
        ans = 1
        for r in range(1, n):
            while s[r] in contains:
                contains.remove(s[l])
                l += 1

            contains.add(s[r])
            ans = max(ans, r - l+ 1)
                    
        return ans

        