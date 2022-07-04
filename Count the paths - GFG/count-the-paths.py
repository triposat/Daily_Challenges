from collections import defaultdict
class Solution:
    def __init__(self):
        self.ans = 0

    def dfs(self, s, d, graph):
        if s == d:
            self.ans += 1
            return
        for x in graph[s]:
            self.dfs(x, d, graph)

    def possible_paths(self, edges, n, s, d):
        res = defaultdict(list)
        for key, val in edges:
            res[key].append(val)
        self.dfs(s, d, res)
        return self.ans
        
        
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