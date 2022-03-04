class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n < 3:
            return None
        nums.sort()
        res = []
        for i in range(n):
            if i == 0 or nums[i] != nums[i-1]:
                tar = -nums[i]
                left = i+1
                right = n-1
                while left < right:
                    add = nums[left]+nums[right]
                    if add == tar:
                        res.append((nums[i], nums[left], nums[right]))
                        left += 1
                        right -= 1
                    elif add > tar:
                        right -= 1
                    else:
                        left += 1
        return set(res)
