class Solution:
    def maxArea(self, h: List[int]) -> int:
        n = len(h)
        left = 0
        ans = -(1 << 31)
        right = n-1
        while left < right:
            hey = (right-left)*(min(h[left], h[right]))
            ans = max(ans, hey)
            if h[left] <= h[right]:
                left += 1
            else:
                right -= 1
        return ans