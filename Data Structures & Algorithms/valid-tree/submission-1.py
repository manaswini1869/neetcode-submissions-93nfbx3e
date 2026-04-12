class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) != n-1:
            return False

        conns = defaultdict(list)
        for a, b in edges:
            conns[a].append(b)
            conns[b].append(a)

        visited = set()
        def dfs(node, parent):
            if node in visited:
                return False
            visited.add(node)
            for nei in conns[node]:
                if nei == parent:
                    continue
                if not dfs(nei, node):
                    return False
            return True

        if not dfs(0, -1):
            return False
        return len(visited) == n


        