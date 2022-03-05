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

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        nums_sum = sum(nums)
        total = (target + nums_sum)
        if abs(target) > nums_sum:
            return 0
        if total % 2 != 0:
            return 0
        else:
            total //= 2
        return self.perfectSum(nums, len(nums), total)