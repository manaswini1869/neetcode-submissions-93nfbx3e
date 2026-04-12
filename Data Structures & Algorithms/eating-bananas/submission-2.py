class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        piles.sort()

        max_k = piles[-1]
        n = len(piles)
        min_k = 1
        k = max_k

        while min_k <= max_k:
            mid = (min_k + max_k) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p/mid)
            if hours > h:
                min_k = mid + 1
            else:
                k = min(k, mid)
                max_k = mid - 1
        return k
        


        



        