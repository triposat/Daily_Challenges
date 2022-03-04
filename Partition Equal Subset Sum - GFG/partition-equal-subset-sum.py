class Solution:
    def equalPartition(self, N, nums):
        total = sum(nums)
        if total % 2 != 0:
            return False
        else:
            total = total//2
        n = len(nums)
        dp = [[0]*(total+1) for _ in range(n+1)]
        for i in range(n+1):
            for j in range(total+1):
                if i == 0:
                    dp[i][j] = False
                if j == 0:
                    dp[i][j] = True
                elif nums[i-1] <= j:
                    dp[i][j] = dp[i-1][j-nums[i-1]] or dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[n][total]

#{ 
#  Driver Code Starts
# Initial Template for Python3

import sys
input = sys.stdin.readline
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for it in range(N):
            arr[it] = int(arr[it])
        
        ob = Solution()
        if (ob.equalPartition(N, arr) == 1):
            print("YES")
        else:
            print("NO")
# } Driver Code Ends