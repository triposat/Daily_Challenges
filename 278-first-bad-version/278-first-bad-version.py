# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        st=0
        end=n
        while st<end:
            mid=(st+end)>>1
            if isBadVersion(mid):
                end=mid
            else:
                st=mid+1
        return st