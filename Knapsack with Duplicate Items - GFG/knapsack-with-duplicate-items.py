#User function Template for python3

class Solution:
    def knapSack(self, n, W, val, wt):
        dp = [[0]*(W+1) for _ in range(n+1)]
        for i in range(n+1):
            for j in range(W+1):
                if i == 0 or j == 0:
                    dp[i][j] = 0
                elif wt[i-1] <= j:
                    dp[i][j] = max(val[i-1]+dp[i][j-wt[i-1]], dp[i-1][j])
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[n][W]

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N, W = [int(x) for x in input().split()]
        val = input().split()
        for itr in range(N):
            val[itr] = int(val[itr])
        wt = input().split()
        for it in range(N):
            wt[it] = int(wt[it])
        
        ob = Solution()
        print(ob.knapSack(N, W, val, wt))
# } Driver Code Ends