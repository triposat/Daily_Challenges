class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l = 0
        r = len(nums)-1
        while l <= r:
            if nums[l] == target or nums[r] == target:
                return True
            elif nums[l] < target:
                while l < r and nums[l] == nums[l+1]:
                    l += 1
                l += 1
            else:
                while l < r and nums[r] == nums[r-1]:
                    r -= 1
                r -= 1
        return False