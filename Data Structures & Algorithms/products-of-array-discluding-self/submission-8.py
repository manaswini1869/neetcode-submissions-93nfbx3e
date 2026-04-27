class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        ans = [1]*n
        prefix = 1
        for i in range(n):
            ans[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(n-1, -1, -1):
            ans[i] *= postfix
            postfix *= nums[i]
        
        return ans

        # for i in range(n):
        #     curr = 1
        #     for j in range(n):
        #         if i != j:
        #             curr *= nums[j]
        #     ans.append(curr)
        # return ans
