class Solution:
    def trap(self, h: List[int]) -> int:
        n = len(h)
        leftMax = [0]*(n)
        rightMax = [0]*(n)
        leftMax[0] = h[0]
        rightMax[n-1] = h[n-1]
        for i in range(1, n):
            leftMax[i] = max(h[i], leftMax[i-1])
        for i in range(n-1)[::-1]:
            rightMax[i] = max(rightMax[i+1], h[i])
        water = 0
        for i in range(n):
            water += min(leftMax[i], rightMax[i])-h[i]
        return water