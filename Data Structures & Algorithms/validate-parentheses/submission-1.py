class Solution:
    def isValid(self, s: str) -> bool:
        paren = {'(':')', '{':'}', '[':']'}
        p = []
        openParen = paren.keys()
        closeParen = paren.values()
        for i in s:
            if i in openParen:
                p.append(paren[i])
            if i in closeParen and len(p)>0:
                p.pop()
            else:
                return False
        if len(p) == 0:
            return True
        else:
            return False
        