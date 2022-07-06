class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return []
        m = len(matrix)
        n = len(matrix[0])
        rowZero = [False]*m
        colZero = [False]*n
        for row in range(m):
            for col in range(n):
                if not matrix[row][col]:
                    rowZero[row] = True
                    colZero[col] = True
        for row in range(m):
            for col in range(n):
                if rowZero[row] or colZero[col]:
                    matrix[row][col] = 0