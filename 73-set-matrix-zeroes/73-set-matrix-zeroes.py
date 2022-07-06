# Space: O(m+n)
# class Solution:
#     def setZeroes(self, matrix: List[List[int]]) -> None:
#         """
#         Do not return anything, modify matrix in-place instead.
#         """
#         if not matrix:
#             return []
#         m = len(matrix)
#         n = len(matrix[0])
#         rowZero = [False]*m # m Space
#         colZero = [False]*n # n Space
#         for row in range(m):
#             for col in range(n):
#                 if not matrix[row][col]:
#                     rowZero[row] = True
#                     colZero[col] = True
#         for row in range(m):
#             for col in range(n):
#                 if rowZero[row] or colZero[col]:
#                     matrix[row][col] = 0
                    
# Space: O(1)
class Solution:
    def setZeroes(self, mat: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not mat:
            return []
        m = len(mat)
        n = len(mat[0])
        rowZero = False
        colZero = False

        # Check for the first Column
        for i in range(m):
            if mat[i][0] == 0:
                colZero = True
                break
        # Check for the first Row
        for j in range(n):
            if mat[0][j] == 0:
                rowZero = True
                break
        # Check except first row and column
        for i in range(1, m):
            for j in range(1, n):
                if mat[i][j] == 0:
                    mat[i][0] = 0
                    mat[0][j] = 0
        # Process except the first row and column
        for i in range(1, m):
            for j in range(1, n):
                if mat[i][0] == 0 or mat[0][j] == 0:
                    mat[i][j] = 0
        # Handle the first row
        if rowZero:
            for i in range(n):
                mat[0][i] = 0
        # Handle the first column
        if colZero:
            for i in range(m):
                mat[i][0] = 0