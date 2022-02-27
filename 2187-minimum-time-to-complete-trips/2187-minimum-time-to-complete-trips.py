class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        def solve(mid):
            res = 0
            for i in time:
                res += mid//i
            return res
        left = 1
        right = totalTrips*min(time)
        while left < right:
            mid = (left+right) >> 1
            if solve(mid) >= totalTrips:
                right = mid
            else:
                left = mid+1
        return left