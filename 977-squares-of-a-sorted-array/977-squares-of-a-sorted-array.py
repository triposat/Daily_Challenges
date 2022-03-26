class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l = 0
        r = n-1
        k = n-1
        res = [0]*n
        for _ in range(n):
            if abs(nums[l]) > abs(nums[r]):
                res[k] = nums[l]*nums[l]
                l += 1
            else:
                res[k] = nums[r]*nums[r]
                r -= 1
            k -= 1
        return res