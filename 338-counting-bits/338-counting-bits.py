class Solution:
    def countBits(self, n: int) -> List[int]:
        memo = [0]*(n+1)

        def solve(n):
            if n == 0:
                return 0
            if n == 1:
                return 1
            if memo[n]:
                return memo[n]
            if n % 2 == 0:
                memo[n] = solve(n//2)
                return memo[n]
            else:
                memo[n] = 1+solve(n//2)
                return memo[n]
        res = [0]*(n+1)
        for i in range(0, n+1):
            res[i] = solve(i)
        return res