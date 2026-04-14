class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        n = len(nums)

        max_ele = max(nums[:k])
        res = []
        l = 1
        for r in range(k-1, n):
            print(nums[r])
            max_ele = max(max_ele, nums[r])
            res.append(max_ele)    
            

        return res


        