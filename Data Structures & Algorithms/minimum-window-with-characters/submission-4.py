class Solution:
    def minWindow(self, s: str, t: str) -> str:

        ns = len(s)
        nt = len(t)

        if ns < nt:
            return ""

        need = Counter(t)
        unique = len(need)
        window = {}
        formed = 0

        best_len = float("inf")
        best_l = 0
        l = 0

        for r in range(len(s)):
            c = s[r]

            window[c] = window.get(c, 0) + 1

            if c in need and window[c] == need[c]:
                formed += 1
            
            while formed == unique:
                if r - l + 1 < best_len:
                    best_len = r - l + 1
                    best_l = l
                
                left_char = s[l]
                window[left_char] -= 1
                if left_char in need and window[left_char] < need[left_char]:
                    formed -= 1
                l += 1
        return "" if best_len == float("inf") else s[best_l:best_l + best_len]

        


        