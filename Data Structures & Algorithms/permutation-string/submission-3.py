class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        n = len(s2)
        s1_sorted = sorted(s1)
        n1 = len(s1_sorted)

        if n < n1:
            return False

        left, right = 0, n1
        while right < n+1:
            sorted_s2 = sorted(s2[left:right])
            if sorted_s2 == s1_sorted:
                return True
            else:
                left += 1
                right += 1
        return False

        # mapper = defaultdict(int)
        # for i in s2:
        #     mapper[i] += 1
        # for j in s1:
        #     if j in mapper and mapper[j] > 0:
        #         mapper[j] -= 1
        #     else:
        #         return False
        # return True

        