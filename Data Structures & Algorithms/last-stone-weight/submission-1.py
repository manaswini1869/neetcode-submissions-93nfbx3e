class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        n = len(stones)
        while n > 1:
            stones.sort()
            cur = stones.pop() - stones.pop()
            if cur > 0:
                stones.append(cur)
                n -= 1
            else:
                stones.append(0)
                n -= 2
        return stones[0]

        