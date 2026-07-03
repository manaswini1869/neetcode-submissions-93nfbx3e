class MinStack:

    def __init__(self):

        self.stack = []
        self.curr_min = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.curr_min:
            self.curr_min.append(val)
        else:
            self.curr_min.append(min(val, self.curr_min[-1]))

    def pop(self) -> None:
        if not self.stack:
            return 
        self.stack.pop()
        self.curr_min.pop()

        

    def top(self) -> int:
        if not self.stack:
            return 
        return self.stack[-1]
        

    def getMin(self) -> int:
        if not self.curr_min:
            return 
        return self.curr_min[-1]
        
