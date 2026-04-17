class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        ans = defaultdict(list)
        for st in strs:
            ste = "".join(sorted(st))
            ans[ste].append(st)

        return list(ans.values())


        