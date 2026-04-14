class MinStack:

    def __init__(self):
        self.stack = []
        self.currMin = float("inf")

    def push(self, val: int) -> None:
        self.currMin = min(self.currMin, val)
        self.stack.append((val, self.currMin))   

    def pop(self) -> None:
        self.stack.pop()
        if stack:
            self.currMin = self.stack[-1][1]
        else:
            self.currMin = float("inf")

    def top(self) -> int:
        return self.stack[-1][0]        

    def getMin(self) -> int:
        return self.stack[-1][1]        
