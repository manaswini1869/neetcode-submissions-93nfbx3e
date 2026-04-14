class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_matix = {}

        for cour, pre in prerequisites:
            if cour in adj_matix:
                return False
            adj_matix[pre] = adj_matix.get(pre, []) + [cour]
        return True


