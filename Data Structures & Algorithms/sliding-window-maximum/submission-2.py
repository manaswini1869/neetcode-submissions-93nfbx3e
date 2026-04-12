class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        n = len(nums)

        max_ele = max(nums[:k])
        res = []
        res.append(max_ele)

        for r in range(k, n):
            l = r - k + 1
            if nums[l-1] == max_ele:
                max_ele = max(nums[l:r+1])
            else:
                max_ele = max(max_ele, nums[r])
            res.append(max_ele)    
            

        return res


        