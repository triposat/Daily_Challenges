class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        # Iterative Approach:
        # if not graph:
        #     return []
        # memo = {}
        # for idx, val in enumerate(graph):
        #     memo[idx] = val
        # stack = [(0, [0])]
        # res = []
        # while stack:
        #     node, path = stack.pop()
        #     if node == len(graph)-1:
        #         res.append(path)
        #     for i in memo[node]:
        #         stack.append((i, path+[i]))
        # return res
    
        # Recursive Approach
        if not graph:
            return []
        res = []


        def solve(node, path):
            if node == len(graph)-1:
                res.append(path)
            for i in graph[node]:
                solve(i, path+[i])


        solve(0, [0])
        return res
