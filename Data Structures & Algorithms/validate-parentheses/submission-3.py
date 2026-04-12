class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        mapper = {
            '}':'{',
            ']':'[',
            ')':'('
        }

        for ch in s:
            if ch in mapper.values():
                stack.append(ch)
            elif ch in mapper.keys():
                if stack and stack[-1] == mapper[ch]:
                    stack.pop()
                else:
                    return False

        return True if not stack else False



        