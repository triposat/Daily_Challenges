class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        q=[]
        m, n = len(mat), len(mat[0])
        for i in range(m):
            for j in range(n):
                if mat[i][j]==1:
                    mat[i][j] = (1<<31)
                else:
                    q.append((i, j))
        for i, j in q:
            for r, c in ((i, j+1), (i, j-1), (i+1, j), (i-1, j)):
                me=mat[i][j]+1
                if 0<=r<m and 0<=c<n and mat[r][c]>me:
                    mat[r][c] = me
                    q.append((r, c))
        return mat