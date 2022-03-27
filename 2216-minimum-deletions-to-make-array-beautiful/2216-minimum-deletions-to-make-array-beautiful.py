class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        cnt = 0
        chnge = 'e'
        n = len(nums)
        for i in range(len(nums)-1):
            if chnge == 'e':
                if i % 2 == 0 and nums[i] == nums[i+1]:
                    cnt += 1
                    chnge = 'o'
            elif chnge == 'o':
                if i % 2 != 0 and nums[i] == nums[i+1]:
                    cnt += 1
                    chnge = 'e'
        if (n-cnt) % 2 != 0:
            cnt += 1
        return cnt