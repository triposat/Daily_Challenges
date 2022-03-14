from heapq import heappush, heappop, heapify
from collections import defaultdict


class Solution:
    def minimumWeight(self, n: int, edges: List[List[int]], s1: int, s2: int, d: int) -> int:
        graph1 = defaultdict(list)
        graph2 = defaultdict(list)
        for s, e, w in edges:
            graph1[s].append((e, w))
            graph2[e].append((s, w))

        def dijkstra(g, s):
            Q = [(0, s)]
            hMap = {}
            heapify(Q)
            while Q:
                wei, node = heappop(Q)
                if node not in hMap:
                    hMap[node] = wei
                    for val, w in g[node]:
                        heappush(Q, (wei+w, val))
            return [hMap.get(i, float("inf")) for i in range(n)]
        res1 = dijkstra(graph1, s1)
        res2 = dijkstra(graph1, s2)
        res3 = dijkstra(graph2, d)
        out = float("inf")
        for i in range(n):
            out = min(out, res1[i]+res2[i]+res3[i])
        return out if out != float("inf") else -1