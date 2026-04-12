from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        t_count = defaultdict(int)
        for ch in t:
            t_count[ch] += 1

        window = defaultdict(int)
        have, need = 0, len(t_count)

        res_len = float("inf")
        res = [-1, -1]

        left = 0
        for right in range(len(s)):
            c = s[right]
            window[c] += 1

            if c in t_count and window[c] == t_count[c]:
                have += 1

            while have == need:
                # update result
                if (right - left + 1) < res_len:
                    res_len = right - left + 1
                    res = [left, right]

                # shrink from left
                window[s[left]] -= 1
                if s[left] in t_count and window[s[left]] < t_count[s[left]]:
                    have -= 1
                left += 1

        l, r = res
        return s[l:r+1] if res_len != float("inf") else ""
