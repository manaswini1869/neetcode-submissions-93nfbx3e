class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        mapper = defaultdict(int)
        for num in nums:
            mapper[num] += 1
        heap = []
        for key, v in mapper.items():
            heapq.heappush(heap, (-v, key))
            if len(heap) >= key:
                heapq.heappop(heap)

        return [key for _, key in heap]



        