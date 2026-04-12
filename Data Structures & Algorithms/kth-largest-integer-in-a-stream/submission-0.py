class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap = nums
        self.k = k
        heapq.heapify(self.minHeap)
        print("1st",self.minHeap)
        while len(self.minHeap) > k:
            print("2st",heapq.heappop(self.minHeap))

    def add(self, val: int) -> int:
        print("3st",self.minHeap)
        heapq.heappush(self.minHeap, val)
        print("4st",self.minHeap)
        if len(self.minHeap) > self.k:
            print("5st",heapq.heappop(self.minHeap))
        return self.minHeap[0]
        
