class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        ans_hash = defaultdict(list)
        for s in strs:
            st = "".join(sorted(s))
            ans_hash[st].append(s)
        
        return list(ans_hash.values())


        