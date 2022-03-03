#User function Template for python3

class Solution:
    def markAll(self, row, col, i, j, grid, dr):
        if i < 0 or i >= row or j < 0 or j >= col:
            return
        self.ans = [i, j]
        if grid[i][j]==0:
            if dr=="R":
                self.markAll(row, col, i, j+1, grid, dr)
            elif dr=="L":
                self.markAll(row, col, i, j-1, grid, dr)
            elif dr=="U":
                self.markAll(row, col, i-1, j, grid, dr)
            else:
                self.markAll(row, col, i+1, j, grid, dr)
        else:
            grid[i][j]=0
            if dr=="R":
                self.markAll(row, col, i+1, j, grid, "D")
            elif dr=="L":
                self.markAll(row, col, i-1, j, grid, "U")
            elif dr=="U":
                self.markAll(row, col, i, j+1, grid, "R")
            else:
                self.markAll(row, col, i, j-1, grid, "L")
        # return ans
                
    def endPoints(self, grid, m, n):
        self.ans =[0,0]
        row = len(grid)
        col = len(grid[0])
        dr="R"
        self.markAll(row, col, 0, 0, grid, dr)
        return self.ans
                
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        r,c = map(int, input().strip().split())
        matrix = []
        for i in range(r):
            line = [int(x) for x in input().strip().split()]
            matrix.append(line)
        ob = Solution()
        ans = ob.endPoints(matrix,r,c)
        print('(',ans[0],', ',ans[1],')',sep ='')

# } Driver Code Ends