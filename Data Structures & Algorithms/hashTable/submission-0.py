class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class HashTable:
    
    def __init__(self, capacity: int):
        self.size = 0
        self.capacity = capacity
        self.map = [None] * capacity

    def hash(self, key):
        if isinstance(key, int):
            return key % self.capacity
        elif isinstance(key, str):
            index = 0
            for c in key:
                index += ord(c)
            return index % self.capacity
        else:
            raise TypeError("Key must be an integer or string")

    def insert(self, key, value) -> None:
        index = self.hash(key)
        while True:
            if self.map[index] is None:
                self.map[index] = Pair(key, value)
                self.size += 1
                if self.size >= self.capacity // 2:
                    self.resize()
                return
            elif self.map[index].key == key:
                self.map[index].value = value
                return
            index = (index + 1) % self.capacity

    def get(self, key) -> int:
        index = self.hash(key)
        while self.map[index] is not None:
            if self.map[index].key == key:
                return self.map[index].value
            index = (index + 1) % self.capacity
        return -1

    def remove(self, key) -> bool:
        index = self.hash(key)
        while self.map[index] is not None:
            if self.map[index].key == key:
                self.map[index] = None
                self.size -= 1
                return True
            index = (index + 1) % self.capacity
        return False

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity

    def resize(self) -> None:
        self.capacity *= 2
        newMap = [None] * self.capacity
        for item in self.map:
            if item is not None:
                index = self.hash(item.key)
                while newMap[index] is not None:
                    index = (index + 1) % self.capacity
                newMap[index] = item
        self.map = newMap
