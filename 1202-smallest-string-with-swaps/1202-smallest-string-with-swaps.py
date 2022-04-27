class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        def dfs(i):
            visit[i]=True
            ans.append(i)
            for j in adj[i]:
                if not visit[j]:
                    dfs(j)
        n=len(s)
        adj = [[] for _ in range(n)]
        for a, b in pairs:
            adj[a].append(b)
            adj[b].append(a)
        visit = [False for _ in range(n)]
        lst = list(s)
        for i in range(n):
            if not visit[i]:
                ans=[]
                dfs(i)
                # print(ans)
                ans.sort()
                chars = [lst[k] for k in ans]
                print(chars)
                chars.sort()
                print(chars)
                for i in range(len(ans)):
                    lst[ans[i]] = chars[i]
        return ''.join(lst)