class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.da = [0]*capacity
        self.length = 0

    def get(self, i: int) -> int:
        return self.da[i]

    def set(self, i: int, n: int) -> None:
        self.da[i] = n

    def pushback(self, n: int) -> None:
        if self.length == self.capacity:
            self.resize()
        idx = self.da.index(n)
        self.da.pop(idx)
        self.da.append(n)

    def popback(self) -> int:
        if self.length > 0:
            self.length -= 1
        return self.da.pop() 

    def resize(self) -> None:
        self.capacity *= 2
        new_arr = [0]*self.capacity
        for i in range(self.length):
            new_arr[i] = self.da[i]
        self.da = new_arr

    def getSize(self) -> int:
        return self.length
    
    def getCapacity(self) -> int:
        return self.capacity
