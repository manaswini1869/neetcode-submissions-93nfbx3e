class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        for token in tokens:
            if token == '+':
                if not stack:
                    return 
                
                b = stack.pop()
                a = stack.pop()
                stack.append(a+b)
            elif token == '-':
                if not stack:
                    return 
                
                b = stack.pop()
                a = stack.pop()
                stack.append(a - b)
            elif token == '*':
                if not stack:
                    return 
                
                b = stack.pop()
                a = stack.pop()
                stack.append(b*a)
            elif token == '/':
                if not stack:
                    return 
                
                b = stack.pop()
                a = stack.pop()
                stack.append(int(a / b))
            else:
                stack.append(int(token))
            print(stack)
        return stack[-1]
        