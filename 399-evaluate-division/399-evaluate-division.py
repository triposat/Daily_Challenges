# BFS Approach

from collections import defaultdict

class Solution:
    def calcEquation(self, e: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)

        def bfs(var):
            vis = set()
            start, end = var
            if start not in graph or end not in graph:
                return -1.0
            que = [(start, 1.0)]
            while que:
                i, j = que.pop(0)
                if i == end:
                    return j
                vis.add(i)
                for char, val in graph[i]:
                    if char not in vis:
                        que.append((char, j*val))
            return -1.0

        for i in range(len(e)):
            graph[e[i][0]].append((e[i][1], values[i]))
            graph[e[i][1]].append((e[i][0], 1/values[i]))
        res = [bfs(q) for q in queries]
        return res
