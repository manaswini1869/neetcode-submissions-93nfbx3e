class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        ans = []

        for i in range(n):
            curr = 1
            for j in range(n):
                if i != j:
                    curr *= nums[j]
            ans.append(curr)
        return ans
                     


        