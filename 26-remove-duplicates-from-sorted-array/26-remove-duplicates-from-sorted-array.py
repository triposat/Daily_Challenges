class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cnt = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[cnt] = nums[i]
                cnt += 1
        return cnt