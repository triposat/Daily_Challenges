class Solution:
    def possible_subA(self, nums, mid):
        add = 0
        cnt = 1
        for i in range(len(nums)):
            if add+nums[i] > mid:
                add = nums[i]
                cnt += 1
            else:
                add += nums[i]
        return cnt

    def splitArray(self, nums: List[int], m: int) -> int:
        low = max(nums)
        high = sum(nums)
        ans = 0
        while low <= high:
            mid = (low+high) >> 1
            n = self.possible_subA(nums, mid)
            if n > m:
                low = mid+1
            else:
                high = mid-1
                ans = mid
        return ans