class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for st in strs:
            n = len(st)
            encoded += str(n)+"#"+st

        return encoded

    def decode(self, s: str) -> List[str]:
        n = len(s)
        i = 0
        ans = []
        while i < n:
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            word = s[j+1:j+length+1]
            ans.append(word)
            i = j + length + 1
        

        return ans
