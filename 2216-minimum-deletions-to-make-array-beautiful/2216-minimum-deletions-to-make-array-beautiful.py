class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        cnt = 0
        n = len(nums)
        for i in range(len(nums)-1):
            if (i+cnt) % 2 == 0:
                if nums[i] == nums[i+1]:
                    cnt += 1
        if (n-cnt) % 2 != 0:
            cnt += 1
        return cnt