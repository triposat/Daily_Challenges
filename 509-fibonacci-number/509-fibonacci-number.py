class Solution:
    def fib(self, n: int) -> int:
        dp = [0]*(n+1)

        def solve(n):
            if n < 2:
                return n
            if dp[n] != 0:
                return dp[n]
            dp[n] = solve(n-1)+solve(n-2)
            return dp[n]
        return solve(n)