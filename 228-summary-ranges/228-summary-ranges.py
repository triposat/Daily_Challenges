class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 1:
            return [f"{nums[0]}"]
        res = []
        i = 0
        while i < len(nums):
            num = nums[i]
            while i+1 < len(nums) and nums[i+1]-nums[i] == 1:
                i += 1
            if num != nums[i]:
                res.append(f"{num}->{nums[i]}")
            else:
                res.append(f"{nums[i]}")
            i += 1
        return res