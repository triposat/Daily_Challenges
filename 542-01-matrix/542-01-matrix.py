class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        que = []
        row, col = len(mat), len(mat[0])
        for i in range(row):
            for j in range(col):
                if mat[i][j] == 1:
                    mat[i][j] = (1 << 31)
                else:
                    que.append((i, j))
        for i, j in que:
            for r, c in ((i, j+1), (i, j-1), (i+1, j), (i-1, j)):
                k = mat[i][j]+1
                if 0 <= r < row and 0 <= c < col and mat[r][c] > k:
                    mat[r][c] = k
                    que.append((r, c))
        return mat
