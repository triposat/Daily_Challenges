class Solution:
    def twoSum(self, nums: List[int], tar: int) -> List[int]:
        left = 0
        right = len(nums)-1
        while left < right:
            if nums[left]+nums[right] == tar:
                return [left+1, right+1]
            elif nums[left]+nums[right] < tar:
                left += 1
            else:
                right -= 1