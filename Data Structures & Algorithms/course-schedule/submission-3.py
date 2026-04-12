class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        course = defaultdict(list)
        for a, b in prerequisites:
            course[b].append(a)
        
        visiting = set()
        visited = set()

        def dfs(cou):
            if cou in visiting:
                return False
            if cou in visited:
                return True
            
            visiting.add(cou)
            
            for nei in course[cou]:
                if not dfs(nei):
                    return False
            visiting.remove(cou)
            visited.add(cou)
            return True                    
            
            

        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True

