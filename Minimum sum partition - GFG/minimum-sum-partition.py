class Solution:
    def minDifference(self, nums, n):
        def isSubsetSum(n, arr, sum):
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
            return dp[-1]
        total = sum(nums)
        outp = isSubsetSum(n, nums, total)
        res = []
        if total % 2 == 0:
            till = len(outp)//2+1
        else:
            till = len(outp)//2
        for i in range(till):
            if outp[i]:
                res.append(i)
        ans = (1 << 31)
        for i in range(len(res)):
            ans = min(ans, total-2*res[i])
        return ans


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N = int(input())
		arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.minDifference(arr, N)
		print(ans)

# } Driver Code Ends