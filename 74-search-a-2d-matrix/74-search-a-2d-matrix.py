class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start = 0
        col = len(matrix[0])
        row = len(matrix)
        end = col-1
        while start<row and end>-1:
            if matrix[start][end]==target:
                return True
            elif matrix[start][end]>target:
                end-=1
            else:
                start+=1
        return False