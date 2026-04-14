class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = " "
        maxLen = 0
        for i in s:
            if i in res:
                maxLen = max(maxLen, len(res))
                res = i
            else:
                print(res)
                res += i
        return maxLen