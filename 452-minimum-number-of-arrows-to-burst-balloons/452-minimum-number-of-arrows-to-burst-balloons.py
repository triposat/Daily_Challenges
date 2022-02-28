class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points)==1:
            return 1
        points.sort()
        # print(points)
        start = points[0][0]
        end = points[0][1]
        res=[]
        i=1
        while i<len(points):
            x, y = points[i][0], points[i][1]
            # print(start, end, x)
            while i<len(points) and points[i][0]<=end:
                start = max(points[i][0], start)
                end = min(points[i][1], end)
                i +=1
            res.append([start, end])
            if i>len(points)-1:
                break
            start = points[i][0]
            end = points[i][1]
            # print(res)
        return len(res)
    
    