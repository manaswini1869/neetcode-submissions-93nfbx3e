class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courses = {i:[] for i in range(numCourses)}
        
        visit_set = set()

        for course, prereq in prerequisites:
            courses[course].append(prereq)

        res = []

        def dfs(course):
            if course in visit_set:
                return False
            if courses[course] == []:
                return True
            
            visit_set.add(course)
            for pre in courses[course]:
                if not dfs(pre):
                    return False
            visit_set.remove(course)
            courses[course] = []            
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
            else:
                res.append(i)
        return res


        

        