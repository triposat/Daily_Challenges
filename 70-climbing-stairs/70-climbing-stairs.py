# Memoization:
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         dp = [0]*(n+1)

#         def solve(n):
#             if n < 4:
#                 return n
#             if dp[n] != 0:
#                 return dp[n]
#             dp[n] = solve(n-1)+solve(n-2)
#             return dp[n]
#         return solve(n)
# Tabulation:
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0]*(n+1)
        dp[0]=1
        dp[1]=1
        for i in range(2, n+1):
            dp[i] = dp[i-1]+dp[i-2]
            print(dp[i])
        return dp[n]