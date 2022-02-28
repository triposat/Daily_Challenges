class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda p: p[1])
        arow = 0
        res = 0
        for start, end in points:
            if res == 0 or start > arow:
                res += 1
                arow = end
        return res