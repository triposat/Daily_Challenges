class Solution:
    def isSubsetSum(self, n, arr, sum):
        dp = [[0]*(sum+1) for _ in range(n+1)]
        for i in range(n+1):
            for j in range(sum+1):
                if i == 0:
                    dp[i][j] = False
                if j == 0:
                    dp[i][j] = True
                elif arr[i-1] <= j:
                    dp[i][j] = dp[i-1][j-arr[i-1]] or dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[n][sum]

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        arr = input().split()
        for itr in range(N):
            arr[itr] = int(arr[itr])
        sum = int(input())

        ob = Solution()
        if ob.isSubsetSum(N,arr,sum)==True:
            print(1)
        else :
            print(0)
            
        

# } Driver Code Ends