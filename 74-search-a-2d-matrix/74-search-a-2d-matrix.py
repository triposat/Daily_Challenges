class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start = 0
        col = len(matrix[0])
        row = len(matrix)
        end = col*row-1
        while start < end:
            mid = (start+end) >> 1
            if matrix[mid//col][mid % col] < target:
                start = mid+1
            else:
                end = mid
        return matrix[start//col][start % col] == target