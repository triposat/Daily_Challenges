class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.ans = set()
        def get_perms(nums, lst):
            if not nums:
                self.ans.add(tuple(lst.copy()))
                return
            for i in range(len(nums)):
                get_perms(nums[:i] + nums[i+1:], lst + [nums[i]])
        get_perms(nums, [])
        return list(self.ans) 