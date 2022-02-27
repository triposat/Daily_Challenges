class Solution:
    def minimumTime(self, time: List[int], tt: int) -> int:
        def solve(mid):
            sum=0
            for hey in time:
                sum+=mid//hey
            return sum
        s=1
        e=tt*min(time)
        while s<e:
            mid = (s+e)>>1
            if solve(mid)>=tt:
                e=mid
            else:
                s=mid+1
        return s