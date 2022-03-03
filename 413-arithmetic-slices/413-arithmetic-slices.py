# O(n) Space
# class Solution:
#     def numberOfArithmeticSlices(self, nums: List[int]) -> int:
#         n = len(nums)
#         if n < 3:
#             return 0
#         memo = [0]*(n)
#         for i in range(2, n):
#             if nums[i]-nums[i-1] == nums[i-1]-nums[i-2]:
#                 memo[i] = memo[i-1]+1
#         return sum(memo)
# O(1) Space
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0
        res = cur = 0
        for i in range(2, n):
            if nums[i]-nums[i-1] == nums[i-1]-nums[i-2]:
                cur += 1
                res += cur
            else:
                cur = 0
        return res
