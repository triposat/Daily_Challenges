# Memoization
class Solution:
    def FindWays(self, n, m, bc):
        mod = 1e9+7

        def solve(n, m, mat, dp, s, e):
            if s > n or e > m or mat[s][e] == False:
                return 0
            if s == n and e == m and mat[s][e] == True:
                return 1
            if dp[s][e] != -1:
                return dp[s][e]
            down = 0
            right = 0
            down = solve(n, m, mat, dp, s+1, e)
            right = solve(n, m, mat, dp, s, e+1)
            dp[s][e] = int((down+right) % mod)
            return dp[s][e]

        dp = [[-1]*(m+1) for _ in range(n+1)]
        mat = [[True]*(m+1) for _ in range(n+1)]
        for i in range(len(bc)):
            x = bc[i][0]
            y = bc[i][1]
            mat[x][y] = False
        return solve(n, m, mat, dp, 1, 1)

	    

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m, k= input().split()
		n = int(n); m = int(m); k = int(k);
		blocked_cells = []
		for i in range(k):
			a = list(map(int, input().split()))
			blocked_cells.append(a)
		obj = Solution()
		ans = obj.FindWays(n, m, blocked_cells)
		print(ans)

# } Driver Code Ends