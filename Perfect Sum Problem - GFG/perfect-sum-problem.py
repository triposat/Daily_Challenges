class Solution:
	def perfectSum(self, nums, n, total):
        n = len(nums)
        dp = [[0]*(total+1) for _ in range(n+1)]
        dp[0][0]=1
        for i in range(1, n+1):
            for j in range(total+1):
                if nums[i-1] <= j:
                    dp[i][j] = dp[i-1][j-nums[i-1]] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        return (dp[n][total])%((10**9)+7)
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n,sum = input().split()
		n,sum = int(n),int(sum)
		arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.perfectSum(arr,n,sum)
		print(ans)

# } Driver Code Ends