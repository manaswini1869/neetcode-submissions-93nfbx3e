class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        n = len(s)

        freq_map = defaultdict(int)
        ans = 0
        left = 0
        max_freq = 0
        for right in range(n):
            freq_map[s[right]] += 1
            max_freq = max(max_freq, freq_map[s[right]])

            while (right - left + 1) - max_freq > k:
                freq_map[s[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans
            


