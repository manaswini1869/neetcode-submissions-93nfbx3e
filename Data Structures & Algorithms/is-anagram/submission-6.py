class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        n = len(s)
        hash1, hash2 = defaultdict(int), defaultdict(int)
        for i, j in zip(s, t):
            hash1[i] += 1
            hash2[j] += 1
        return hash1 == hash2



        