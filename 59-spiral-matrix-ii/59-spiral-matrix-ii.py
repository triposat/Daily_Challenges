class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        mat = [[0]*n for _ in range(n)]
        row_bg = 0
        col_bg = 0
        row_end = len(mat)
        col_end = len(mat[0])
        val=1
        while row_bg < row_end and col_bg < col_end:
            for i in range(col_bg, col_end):
                mat[row_bg][i] = val
                val+=1
            row_bg += 1
            for i in range(row_bg, row_end):
                mat[i][col_end-1]=val
                val+=1
            col_end -= 1
            if row_bg < row_end:
                for i in range(col_end-1, col_bg-1, -1):
                    mat[row_end-1][i]= val
                    val+=1
            row_end -= 1
            if col_bg < col_end:
                for i in range(row_end-1, row_bg-1, -1):
                    mat[i][col_bg] = val
                    val+=1
            col_bg += 1
        return mat