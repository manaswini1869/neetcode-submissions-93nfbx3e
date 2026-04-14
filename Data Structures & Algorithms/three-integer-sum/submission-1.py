class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        n = len(nums)

        def dfs(curr, start, limit):
            if limit != 2:
                for i in range(start, n):
                    if i > start and nums[i] == nums[i - 1]:
                        continue
                    curr.append(nums[i])
                    dfs(curr, i + 1, limit - 1)
                    curr.pop()
            else:
                hash_map = set()
                target = -sum(curr)
                for i in range(start, n):
                    if target - nums[i] in hash_map:
                        ans.append(curr + [nums[i], target - nums[i]])
                    hash_map.add(nums[i])

        dfs([], 0, 3)
        return ans
