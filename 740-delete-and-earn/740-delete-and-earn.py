class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        earn = {}
        for i in nums:
            earn[i] = earn.get(i, 0)+i
        max_num = max(nums)
        two_back = 0
        one_back = earn.get(1, 0)
        for i in range(2, max_num+1):
            two_back, one_back = one_back, max(
                one_back, two_back+earn.get(i, 0))
        return one_back