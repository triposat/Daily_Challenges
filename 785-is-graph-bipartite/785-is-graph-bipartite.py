class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = {}

        def dfs(j):
            for k in graph[j]:
                if k not in color:
                    color[k] = 1-color[j]
                    if not dfs(k):
                        return False
                else:
                    if color[k] == color[j]:
                        return False
            return True
        for i in range(len(graph)):
            if i not in color:
                color[i] = 0
                if not dfs(i):
                    return False
        return True