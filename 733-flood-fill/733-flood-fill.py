class Solution:
    def floodFill(self, nums: List[List[int]], sr: int, sc: int, new: int) -> List[List[int]]:
        def solve(row, col, i, j, new, grid, pas):
            if i < 0 or i >= row or j < 0 or j >= col or grid[i][j] != pas:
                return
            grid[i][j] = new
            solve(row, col, i, j-1, new, grid, pas)
            solve(row, col, i, j+1, new, grid, pas)
            solve(row, col, i-1, j, new, grid, pas)
            solve(row, col, i+1, j, new, grid, pas)
            # print(grid)
        row = len(nums)
        col = len(nums[0])
        pas = nums[sr][sc]
        if pas==new:
            return nums
        solve(row, col, sr, sc, new, nums, pas)
        return nums