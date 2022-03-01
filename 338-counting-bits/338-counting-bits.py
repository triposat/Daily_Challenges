class Solution:
    def countBits(self, n: int) -> List[int]:
        def solve(n):
            if n==0:
                return 0
            if n==1:
                return 1
            if n%2==0:
                return solve(n//2)
            else:
                return 1+solve(n//2)
        res=[0]*(n+1)
        for i in range(0, n+1):
            res[i] = solve(i)
        return res