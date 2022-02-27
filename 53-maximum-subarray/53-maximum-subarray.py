class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = 0
        res = -(1 << 31)
        for ele in nums:
            curr += ele
            res = max(res, curr)
            if curr < 0:
                curr = 0
        return res