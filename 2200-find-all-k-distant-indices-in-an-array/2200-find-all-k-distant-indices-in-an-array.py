class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        res = []
        for i in range(len(nums)):
            if nums[i] == key:
                res.append(i)
        out = []
        for i in range(len(nums)):
            for j in res:
                diff = i-j
                if abs(diff) <= k:
                    out.append(i)
                    break
        return out