class Solution:
    def kvowelwords(self, n, k):
        mod = 1000000007
        dp = [[1]*(k+1) for _ in range(n+1)]
        for i in range(1, n+1):
            for j in range(0, k+1):
                if j == 0:
                    dp[i][j] = (21*dp[i-1][k]) % mod
                else:
                    dp[i][j] = (21*dp[i-1][k] % mod+5*dp[i-1][j-1] % mod) % mod
        return dp[n][k]
        
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N,K = map(int,input().split())
		ob = Solution()
		ans = ob.kvowelwords(N,K)
		print(ans)
# } Driver Code Ends