# Greedy Method
# Time: O(n)
# Space: O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curSum = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                curSum += prices[i]-prices[i-1]
        return curSum