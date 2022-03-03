class Solution:
    def markAll(self, row, col, i, j, grid):
        if i < 0 or i >= row or j < 0 or j >= col or grid[i][j] != 1:
            return 0
        grid[i][j] = 2
        a = self.markAll(row, col, i, j-1, grid) +1
        b = self.markAll(row, col, i, j+1, grid) +1
        c = self.markAll(row, col, i-1, j, grid)+1
        d = self.markAll(row, col, i+1, j, grid)+1
        return (a+b+c+d)

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        num = 0
        cnt=0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    num = max(num, self.markAll(row, col, i, j, grid))
        return num//4
    