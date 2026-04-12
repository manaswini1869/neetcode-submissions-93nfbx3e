class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        conns = defaultdict(list)
        for a, b in edges:
            conns[a].append(b)
            conns[b].append(a)

        visited = set()
        graphs = []

        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for nei in conns[node]:
                dfs(nei)

        res = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                res += 1

        return res
        