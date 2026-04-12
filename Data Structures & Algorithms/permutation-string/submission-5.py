class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        n = len(s2)
        n1 = len(s1)

        if n < n1:
            return False

        char_freq1 = [0]*26
        char_freq2 = [0]*26
        for ch in range(n1):
            char_freq1[ord(s1[ch]) - ord('a')] += 1
            char_freq2[ord(s2[ch]) - ord('a')] += 1
        matched = 0
        for i in range(26):
            if char_freq1[i] == char_freq2[i]:
                matched += 1
        l = 0
        for r in range(n1, n):
            if matched == 26:
                return True
            
            index = ord(s2[r]) - ord('a')
            char_freq2[index] += 1
        
            if char_freq1[index] == char_freq2[index]:
                matched += 1
            elif char_freq1[index] + 1 == char_freq2[index]:
                matched -= 1
            
            index = ord(s2[l]) - ord('a')
            char_freq2[index] -= 1
        
            if char_freq1[index] == char_freq2[index]:
                matched += 1
            elif char_freq1[index] - 1 == char_freq2[index]:
                matched -= 1
            l += 1
        return matched == 26
        

        



        # left, right = 0, n1
        # while right < n+1:
        #     sorted_s2 = sorted(s2[left:right])
        #     if sorted_s2 == s1_sorted:
        #         return True
        #     else:
        #         left += 1
        #         right += 1
        # return False

        # mapper = defaultdict(int)
        # for i in s2:
        #     mapper[i] += 1
        # for j in s1:
        #     if j in mapper and mapper[j] > 0:
        #         mapper[j] -= 1
        #     else:
        #         return False
        # return True

        