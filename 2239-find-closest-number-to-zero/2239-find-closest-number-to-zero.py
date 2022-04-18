class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        ans = nums[0]
        for n in nums:
            if abs(n-0.1) < abs(ans-0.1):
                ans = n
        return ans