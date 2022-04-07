class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for ele in nums:
            ele = abs(ele)
            if nums[ele]<0:
                return ele
            nums[ele] = -nums[ele]
        