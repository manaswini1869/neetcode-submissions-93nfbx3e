class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        ans, ansStr = [], ""
        for str1 in strs:
            ans.append(len(str1))
        for sz in ans:
            ansStr += str(sz)
            ansStr += ","
        ansStr += "#"
        for s in strs:
            ansStr += s
        return ansStr

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        sizes, res, i = [], [], 0
        while s[i]!="#":
            cur = ""
            while s[i] != ",":
                cur += s[i]
                i += 1
            sizes.append(int(cur))
            i+=1
        i+=1
        for sz in sizes:
            res.append(s[i:i + sz])
            i += sz
        return res

