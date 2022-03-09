class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        que = []
        row, col = len(grid), len(grid[0])
        fresh = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    que.append((i, j))
        if not fresh:
            return 0
        res = 0
        while que:
            res += 1
            for _ in range(len(que)):
                i, j = que.pop(0)
                for r, c in ((i, j+1), (i, j-1), (i+1, j), (i-1, j)):
                    if 0 <= r < row and 0 <= c < col and grid[r][c] == 1:
                        grid[r][c] = 2
                        fresh -= 1
                        que.append((r, c))

        return -1 if fresh else max(0, res-1)