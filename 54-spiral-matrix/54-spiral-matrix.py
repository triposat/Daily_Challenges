class Solution:
    def spiralOrder(self, mat: List[List[int]]) -> List[int]:
        res = []
        if not mat:
            return res
        row_bg = 0
        col_bg = 0
        row_end = len(mat)
        col_end = len(mat[0])
        while row_bg < row_end and col_bg < col_end:
            for i in range(col_bg, col_end):
                res.append(mat[row_bg][i])
            row_bg += 1
            for i in range(row_bg, row_end):
                res.append(mat[i][col_end-1])
            col_end -= 1
            if row_bg < row_end:
                for i in range(col_end-1, col_bg-1, -1):
                    res.append(mat[row_end-1][i])
            row_end -= 1
            if col_bg < col_end:
                for i in range(row_end-1, row_bg-1, -1):
                    res.append(mat[i][col_bg])
            col_bg += 1
        return res