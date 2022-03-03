# Memoization
class Solution:
    # Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self, W, wt, val, n):
        dp = [[-1]*(W+1) for _ in range(n+1)]

        def solve(W, wt, val, n):
            if W == 0 or n == 0:
                dp[n][W] = 0
                return dp[n][W]
            if dp[n][W] != -1:
                return dp[n][W]
            if wt[n-1] <= W:
                dp[n][W] = max(val[n-1]+solve(W-wt[n-1], wt,
                                              val, n-1), solve(W, wt, val, n-1))
            elif wt[n-1] > W:
                dp[n][W] = solve(W, wt, val, n-1)
            return dp[n][W]

        return solve(W, wt, val, n)

# Top-down Approach
class Solution:
    # Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self, W, wt, val, n):
        dp = [[0]*(W+1) for _ in range(n+1)]
        for i in range(n+1):
            for j in range(W+1):
                if i == 0 or j == 0:
                    dp[i][j] = 0
                elif wt[i-1] <= j:
                    dp[i][j] = max(val[i-1]+dp[i-1][j-wt[i-1]], dp[i-1][j])
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[n][W]

        
#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        W = int(input())
        val = list(map(int,input().strip().split()))
        wt = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.knapSack(W,wt,val,n))
# } Driver Code Ends