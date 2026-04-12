class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # greedy
        n = len(nums)
        goal = n - 1
        for i in range(n-2, -1, -1):
            for j in range(1, nums[i]+1):
                if i + j >= goal:
                    goal = i


            
        return goal == 0



        # dp bottom - up
        
        