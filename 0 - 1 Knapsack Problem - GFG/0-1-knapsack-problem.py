class Solution:
    # Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self, W, wt, val, n):
        def solve(W, wt, val, n, dp):
            if W == 0 or n == 0:
                dp[n][W]=0
                return dp[n][W]
            if dp[n][W]!=-1:
                return dp[n][W]
            else:
                if wt[n-1] <= W:
                    dp[n][W] = max(val[n-1]+solve(W-wt[n-1], wt, val, n-1, dp), solve(W, wt, val, n-1, dp))
                elif wt[n-1] > W:
                     dp[n][W] = solve(W, wt, val, n-1, dp)
            return dp[n][W]
        dp=[[-1]*(W+1) for _ in range(n+1)]
        return solve(W, wt, val, n, dp)

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