# Math
import math
class Solution:
    def countOrders(self, n: int) -> int:
        return (math.factorial(2*n) >> n) % ((10**9)+7)
    
# Dynamic Programming
class Solution:
    def countOrders(self, n: int) -> int:
        dp = [0 for i in range(n+1)]
        dp[0] = 1
        for i in range(1, n+1):
            gaps = 2*i+1
            dp[i] = dp[i-1]*(gaps*(gaps+1))//2
        return dp[n-1] % ((10**9)+7)