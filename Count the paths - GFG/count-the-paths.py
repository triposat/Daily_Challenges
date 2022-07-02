#User function Template for python3
from collections import defaultdict
class Solution:
    def possible_paths(self, edges, n, s, d):
        g = defaultdict(set)
        for frm, to in edges:
            g[frm].add(to)
            
        cnt = 0
        def dfs(node):
            nonlocal d, cnt
            if node == d:
                cnt += 1
                return
            
            for nbr in g[node]:
                dfs(nbr)
        
        dfs(s)
        return cnt

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m, s, d = input().split()
		n = int(n); m = int(m); s = int(s); d = int(d);
		edges = []
		for _ in range(m):
		    x,y = input().split()
		    x = int(x); y = int(y);
		    edges.append([x,y])
		obj = Solution()
		ans = obj.possible_paths(edges, n, s, d)
		print(ans)


# } Driver Code Ends