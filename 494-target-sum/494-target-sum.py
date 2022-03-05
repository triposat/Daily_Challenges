class Solution:
    def perfectSum(self, nums, n, total):
        dp = [[0]*(total+1) for _ in range(n+1)]
        # dp[0][0] = 1
        sum_to=(total + sum(nums))
        for i in range(n+1):
            dp[i][0] = 1 
        # for i in range(1,sum_to+1):
        #     dp[0][i] = 0 
        for i in range(1, n+1):
            for j in range(total+1):
                # if i == 0:
                #     dp[i][j] = 1
                # if j == 0:
                #     dp[i][j] = 1
                if nums[i-1] <= j:
                    dp[i][j] = dp[i-1][j-nums[i-1]] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        return (dp[n][total])
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        if target<0 and len(nums)==1 and nums[0]==abs(target):
            return 1
        if target<0 and len(nums)==1:
            return 0
        hey  = (target + sum(nums))
        if hey%2 != 0:
            return 0
        hey//=2
        return self.perfectSum(nums, len(nums), hey)