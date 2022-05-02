from heapq import heappop, heappush, heapify


class Solution:
    def minimumEffortPath(self, h: List[List[int]]) -> int:
        direc = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        row = len(h)
        col = len(h[0])
        pq = []
        heapify(pq)
        ans = 0
        heappush(pq, (0, 0, 0))
        while pq:
            ele = heappop(pq)
            ans = max(ans, ele[0])
            i = ele[1]
            j = ele[2]
            if h[i][j] == -1:
                continue
            if i == row-1 and j == col-1:
                break
            for di in direc:
                newi = i+di[0]
                newj = j+di[1]
                if newi < 0 or newi >= row or newj < 0 or newj >= col:
                    continue
                heappush(pq, (abs(h[newi][newj]-h[i][j]), newi, newj))
            h[i][j] = -1
        return ans