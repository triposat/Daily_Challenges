class Solution:
    def maximumCandies(self, cand: List[int], k: int) -> int:
        s=0
        e=sum(cand)
        while s<e:
            ans=0
            mid = (s+e+1)>>1
            for i in cand:
                ans+=i//mid
            if ans>=k:
                s=mid
            else:
                e=mid-1
        return s