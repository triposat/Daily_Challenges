class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        prev = nums[0]
        right = 0
        for i in range(1, len(nums)):
            if nums[i] < prev:
                right = i
            else:
                prev = nums[i]
        prev = nums[-1]
        for i in range(len(nums)-1)[::-1]:
            if nums[i] > prev:
                left = i
            else:
                prev = nums[i]
        if right == 0:
            return 0
        return right-left+1