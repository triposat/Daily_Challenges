class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        def dfs(i):
            visit[i] = True
            res.append(i)
            for j in adj[i]:
                if not visit[j]:
                    dfs(j)
        n = len(s)
        adj = [[] for _ in range(n)]
        for a, b in pairs:
            adj[a].append(b)
            adj[b].append(a)
        visit = [False for _ in range(n)]
        lst = list(s)
        for i in range(n):
            if not visit[i]:
                res = []
                dfs(i)
                res.sort()
                char = [lst[j] for j in res]
                char.sort()
                for k in range(len(res)):
                    lst[res[k]] = char[k]
        return "".join(lst)