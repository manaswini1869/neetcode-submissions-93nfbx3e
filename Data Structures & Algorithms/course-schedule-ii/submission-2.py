class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        courses = defaultdict(list)
        for a, b in prerequisites:
            courses[b].append(a)

        visiting = set()
        visited = set()
        answer = []
        def dfs(c):
            if c in visiting:
                return False
            if c in visited:
                return True

            visiting.add(c)
            for n in courses[c]:
                if not dfs(n):
                    return False
            visiting.remove(c)
            visited.add(c)
            answer.append(c)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return []

        return answer[::-1]
            

