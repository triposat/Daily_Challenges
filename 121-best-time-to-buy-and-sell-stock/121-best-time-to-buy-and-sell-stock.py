class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        miN = (1 << 31)
        maX = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                miN = min(miN, prices[i-1])
                maX = max(maX, prices[i]-miN)
        return maX