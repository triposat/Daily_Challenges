class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [None]*numRows
        for i in range(numRows):
            res[i] = [None]*(i+1)
            res[i][0] = res[i][i] = 1
            for j in range(1, i):
                res[i][j] = res[i-1][j-1]+res[i-1][j]
        return res