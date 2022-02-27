class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        minS = (1 << 31)
        minSum = 0
        maxS = -(1 << 31)
        totSum = 0
        maxSum = 0
        for ele in nums:
            totSum += ele
            # Maximum Sum Subarray...
            maxSum += ele
            maxS = max(maxS, maxSum)
            if maxSum < 0:
                maxSum = 0
            # ...
            # Minimum Sum Subarray...
            minSum += ele
            minS = min(minS, minSum)
            if minSum > 0:
                minSum = 0
            # ...
        if(totSum == minS):
            return maxS
        return max(maxS, (totSum-minS))