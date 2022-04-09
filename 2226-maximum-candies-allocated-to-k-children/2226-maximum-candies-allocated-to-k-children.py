class Solution:
    def maximumCandies(self, cand: List[int], k: int) -> int:
        left = 0
        right = sum(cand)
        while left < right:
            ans = 0
            mid = (left+right+1) >> 1
            for i in cand:
                ans += i//mid
            if ans >= k:
                left = mid
            else:
                right = mid-1
        return left