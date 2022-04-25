class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        s = set()
        for cir in circles:
            x = cir[0]
            y = cir[1]
            r = cir[2]
            for x1 in range(x-r, x+r+1):
                for y1 in range(y-r, y+r+1):
                    if (x1-x)*(x1-x)+(y1-y)*(y1-y) <= r*r:
                        s.add((x1, y1))
        return len(s)