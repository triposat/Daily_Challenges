class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = 0
        r = len(nums)-1
        k = len(nums)-1
        res = [0]*len(nums)
        for i in range(len(nums)):
            if abs(nums[l]) > abs(nums[r]):
                res[k] = nums[l]*nums[l]
                l += 1
            else:
                res[k] = nums[r]*nums[r]
                r -= 1
            k -= 1
        return res