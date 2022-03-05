class Solution:
    def perfectSum(self, nums, n, total):
        dp = [[0]*(total+1) for _ in range(n+1)]
        for i in range(n+1):
            dp[i][0] = 1
        for i in range(1, n+1):
            for j in range(total+1):
                if nums[i-1] <= j:
                    dp[i][j] = dp[i-1][j-nums[i-1]] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        return (dp[n][total])

    def findTargetSumWays(self, nums, n, target):
        nums_sum = sum(nums)
        total = (target + nums_sum)
        if total % 2 != 0 or abs(target) > nums_sum:
            return 0
        else:
            total //= 2
        return self.perfectSum(nums, len(nums), total)


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        arr=list(map(int,input().split()))
        target = int(input())
        ob = Solution()
        print(ob.findTargetSumWays(arr,N, target))
# } Driver Code Ends