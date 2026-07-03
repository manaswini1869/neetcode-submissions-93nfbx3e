class Solution:
    def isValid(self, s: str) -> bool:
        
        if len(s) < 2:
            return False

        stack = []
        mapping = {')':'(', '}':'{', ']':'['}

        for brac in s:
            if brac in mapping.values():
                stack.append(brac)
            else:
                if stack:
                    curr = stack.pop()
                else:
                    return False 
                if curr != mapping[brac]:
                    return False
        return len(stack) == 0


        