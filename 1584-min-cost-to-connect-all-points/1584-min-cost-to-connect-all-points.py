class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        hashMap = {}
        for idx, (x, y) in enumerate(points):
            if idx:
                hashMap[(x, y)] = float('inf')
            else:
                hashMap[(x, y)] = 0
        res = 0
        while hashMap:
            x, y = min(hashMap, key=hashMap.get)
            res += hashMap.pop((x, y))
            for x1, y1 in hashMap:
                hashMap[(x1, y1)] = min(hashMap[(x1, y1)], abs(x-x1)+abs(y-y1))
        return res