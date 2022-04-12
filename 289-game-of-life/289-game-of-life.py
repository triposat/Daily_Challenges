class Solution:
    def markAll(self, i, j, grid):
        direc = [[1, 0], [-1, 0], [0, 1], [0, -1],
                 [1, 1], [1, -1], [-1, 1], [-1, -1]]
        cnt = 0
        row = len(grid)
        col = len(grid[0])
        die = 3
        for dire in direc:
            x = i+dire[0]
            y = j+dire[1]
            if x >= 0 and y >= 0 and x < row and y < col:
                if grid[x][y] == 1 or grid[x][y] == die:
                    cnt += 1
        return cnt

    def gameOfLife(self, grid: List[List[int]]) -> None:
        """
        Do not return anything, modify grid in-place instead.
        """
        live = 2
        die = 3
        row = len(grid)
        col = len(grid[0])
        for i in range(row):
            for j in range(col):
                cnt = self.markAll(i, j, grid)
                if cnt == 3 and grid[i][j] == 0:
                    grid[i][j] = live
                elif grid[i][j] == 1:
                    if cnt < 2 or cnt > 3:
                        grid[i][j] = die
        for i in range(row):
            for j in range(col):
                if grid[i][j] == live:
                    grid[i][j] = 1
                if grid[i][j] == die:
                    grid[i][j] = 0