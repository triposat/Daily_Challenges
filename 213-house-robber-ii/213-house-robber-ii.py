class Solution:
    def final(self, nums):
        n = len(nums)
        two_back = 0
        one_back = 0
        for i in range(n):
            two_back, one_back = one_back, max(
                one_back, two_back+nums[i])
        return one_back

    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        return max(self.final(nums[:-1]), self.final(nums[1:]))