# Time: O(n) - But Two loops!
# Space: O(1)
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        prev = nums[0]
        right = 0
        for i in range(1, len(nums)):
            if nums[i] < prev:
                right = i
            else:
                prev = nums[i]
        prev = nums[-1]
        for i in range(len(nums)-1)[::-1]:
            if nums[i] > prev:
                left = i
            else:
                prev = nums[i]
        if right == 0:
            return 0
        return right-left+1

# Time: O(n) - One loop!
# Space: O(1)
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        lprev = nums[0]
        rprev = nums[-1]
        right = 0
        for i in range(1, len(nums)):
            if nums[i] < lprev:
                right = i
            else:
                lprev = nums[i]
            if nums[~i] > rprev:
                left = ~i
            else:
                rprev = nums[~i]
        if right == 0:
            return 0
        return right-(len(nums)+left)+1