class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        maxS = -(1 << 31)
        minS = (1 << 31)
        sum = 0
        maxSum=0
        minSum=0
        for ele in nums:
            sum += ele
            maxSum += ele
            maxS = max(maxS, maxSum)
            if maxSum < 0:
                maxSum = 0
            minSum += ele
            minS = min(minS, minSum)
            if minSum > 0:
                minSum = 0
        if(sum==minS):
            return maxS
        return max(maxS,(sum-minS))
    