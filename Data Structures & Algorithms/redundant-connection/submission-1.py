class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        conns = defaultdict(list)
        n = len(edges)

        


        def dfs(node, parent):            
            if visited[node]:
                return True

            visited[node] = True
            for nei in conns[node]:
                if nei == parent:
                    continue
                if dfs(nei, node):
                    return True
            
            return False
            

        for a, b in edges:
            conns[a].append(b)
            conns[b].append(a)
            visited = [False] * (n+1)
            if dfs(a, -1):
                return [a, b]

            


        return []





        