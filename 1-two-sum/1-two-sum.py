class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hMap = {}
        for idx, val in enumerate(nums):
            rem = target-val
            if rem in hMap:
                return [hMap[rem], idx]
            hMap[val] = idx