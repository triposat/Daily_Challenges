class Solution:
    def canPartition(self, nums: List[int]) -> bool:
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