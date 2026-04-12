class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        
        n1 = len(s)
        n2 = len(t)
        if n1 < n2:
            return ""
        
        mapper_t = defaultdict(int)
        window = defaultdict(int)
        for i in t:
            mapper_t[i] += 1
        max_len = float("inf")
        need, have = len(mapper_t), 0
        res = [-1, -1]
        left = 0
        for right in range(n1):
            c = s[right]
            window[c] += 1
            if c in mapper_t and mapper_t[c] == window[c]:
                have += 1
            while need == have:
                if max_len > (right - left + 1):
                    max_len = right - left + 1
                    res = [left, right]
                window[s[left]] -= 1
                if s[left] in mapper_t and window[s[left]] < mapper_t[s[left]]:
                    have -= 1
                left += 1
        l, r = res
        return s[l:r+1] if max_len != float("inf") else ""
        