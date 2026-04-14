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

        size = s.split('#')
        if not size:
            return []
        sizes = size[0].split(',')
        sizes.pop()
        rem = size[1]
        ans = []
        k = 0
        
        for i in sizes:
            j = int(i)
            ans.append(rem[k:k+j])
            k += j

        return ans

