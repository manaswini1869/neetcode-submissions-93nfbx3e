class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        n = len(s)
        if n == 1:
            return n

        ans = float("-inf")

        left, right = 0, 0
        tracker = defaultdict(int)
        max_f = 0
        while right < n:
            tracker[s[right]] += 1
            max_f = max(max_f, tracker[s[right]])
            while (right - left + 1) - max_f > k:
                tracker[s[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
            right += 1

        return ans
