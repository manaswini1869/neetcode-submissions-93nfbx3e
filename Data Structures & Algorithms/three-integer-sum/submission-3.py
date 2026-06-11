class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        nums.sort()
        res = []
        for i in range(n):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            l, r = i+1, n-1

            while l < r:
                if nums[l] + nums[r] == -1*nums[i]:
                    res.append([nums[l], nums[r], nums[i]])
                    l += 1
                    r -= 1
                    while l < r and nums[l-1] == nums[l]:
                        l += 1
                
                elif nums[l] + nums[r] > -1*nums[i]:
                    r -= 1
                else:
                    l += 1
        return res



        