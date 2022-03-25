class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = 0
        right = sum(nums)
        for idx, val in enumerate(nums):
            right -= val
            if left == right:
                return idx
            left += val
        return -1