class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        # Iterative Approach:
        if not graph:
            return []
        hey={}
        for idx, val in enumerate(graph):
            hey[idx]=val
        stack=[(0, [0])]
        res=[]
        while stack:
            node, path = stack.pop()
            if node==len(graph)-1:
                res.append(path)
            for me in hey[node]:
                stack.append((me, path+[me]))
        return res
        