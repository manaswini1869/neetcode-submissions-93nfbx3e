class MedianFinder:

    def __init__(self):
        self.medium_ints = []
        self.length = 0

    def addNum(self, num: int) -> None:
        self.length += 1
        self.medium_ints.append(num)

    def findMedian(self) -> float:
        if self.length > 0:
            self.medium_ints.sort()
            if self.length % 2 == 0:
                n = self.length // 2
                return (self.medium_ints[n] + self.medium_ints[n-1]) / 2
            else:
                return (self.medium_ints[self.length // 2])
        