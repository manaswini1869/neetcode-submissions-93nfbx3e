class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hash_ans = defaultdict(int)
        first, second = -1, -1

        for k, v in enumerate(nums):
            if target - v in hash_ans:
                first = hash_ans[target - v]
                second = k
            hash_ans[v] = k
        return [first, second]



        