class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans, curr = [], []
        n = len(nums)

        def dfs(start, target, limit):
            if limit != 2:
                for i in range(start, n):
                    if i > start and nums[i] == nums[i - 1]:
                        continue
                    curr.append(nums[i])
                    dfs(i+1, target-nums[i], limit - 1)
                    curr.pop()
                return
            l, r = start, n-1
            while l < r:
                if nums[l] + nums[r] < target:
                    l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    ans.append((curr + [nums[l], nums[r]]))
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1            


        dfs(0, 0, 3)
        return ans
