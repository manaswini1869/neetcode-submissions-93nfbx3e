class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        n = len(s)
        m = len(t)
        if n != m:
            return False
        
        hash_s, hash_t = {}, {}
        for i in range(n):
            hash_s[s[i]] = hash_s.get(s[i], 0) + 1
            hash_t[t[i]] = hash_t.get(t[i], 0) + 1
        
        for k in s:
            if k not in hash_t or hash_s[k] != hash_t[k]:
                return False

        return True



        