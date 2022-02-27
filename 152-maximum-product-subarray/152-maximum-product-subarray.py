import sys
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = -sys.maxsize
        prod = 1
        for i in range(len(nums)):
            prod *= nums[i]
            ans = max(prod, ans)
            if prod == 0:
                prod = 1
        prod = 1
        for i in range(len(nums)-1, 0, -1):
            prod *= nums[i]
            ans = max(prod, ans)
            if prod == 0:
                prod = 1
        return ans
            
        