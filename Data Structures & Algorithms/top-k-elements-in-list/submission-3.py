class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        mapper = defaultdict(int)
        for num in nums:
            mapper[num] += 1
        heap = []
        for key, freq in mapper.items():
            heapq.heappush(heap, (freq, key))
            if len(heap) > k:
                heapq.heappop(heap)

        return [val for _, val in heap]



        