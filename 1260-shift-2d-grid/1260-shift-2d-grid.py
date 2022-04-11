# class Solution:
#     def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
#         m=len(grid)
#         n=len(grid[0])
#         hey = grid[-1][-1]
#         me = grid[0].pop()
#         for i in range(k):
#             for j in range(1, m):
#                 grid[j].insert(0, me)
#                 me = grid[j].pop()
#             grid[0].insert(0, me)
#         return grid

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
            k = k % (len(grid) * len(grid[0]))
            print(k)
            for _ in range(k):
                for i in range(len(grid)):
                    grid[i] = [grid[i-1].pop()] + grid[i]
            return grid