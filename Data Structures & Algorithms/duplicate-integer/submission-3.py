class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        so_far = set()
        for i in nums:
            if i in so_far:
                return True
            so_far.add(i)
        return False




        