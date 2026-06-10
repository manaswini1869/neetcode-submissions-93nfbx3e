class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
            
        n = len(numbers)
        index_map = defaultdict(int)
        for idx, num in enumerate(numbers):
            if target - num in index_map:
                return [index_map[target-num], idx+1]
            index_map[num] = idx+1


        return []



        


        