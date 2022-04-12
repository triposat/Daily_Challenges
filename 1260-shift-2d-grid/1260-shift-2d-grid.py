class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        k = k % (m*n)
        for _ in range(k):
            for j in range(m):
                grid[j].insert(0, grid[j-1].pop())
        return grid