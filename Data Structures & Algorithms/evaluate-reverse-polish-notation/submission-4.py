class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        valid = set(('+','-','/','*'))
        stack = []
        
        for ch in tokens:
            if ch in valid:
                if ch == '+':
                    a, b = stack.pop(), stack.pop()
                    stack.append(a+b)
                elif ch == '-':
                    a, b = stack.pop(), stack.pop()
                    stack.append(b-a)
                elif ch == '*':
                    a, b = stack.pop(), stack.pop()
                    stack.append(a*b)
                else:
                    a, b = stack.pop(), stack.pop()
                    stack.append(b//a)
            else:
                stack.append(int(ch))
        return stack[-1]




        