class Solution:
    def orangesRotting(self, mat: List[List[int]]) -> int:
        que = []
        row, col = len(mat), len(mat[0])
        fresh=0
        for i in range(row):
            for j in range(col):
                if mat[i][j] == 1:
                    fresh+=1
                elif mat[i][j]==2:
                    que.append((i, j))
        if not fresh:
            return 0
        # print(que, fresh)
        res=0
        while que:
            res+=1
            for _ in range(len(que)):
                i, j = que.pop(0)
                for r, c in ((i, j+1), (i, j-1), (i+1, j), (i-1, j)):
                    if 0 <= r < row and 0 <= c < col and mat[r][c] == 1:
                        mat[r][c] = 2
                        fresh-=1
                        que.append((r, c))
            
        return -1 if fresh else max(0, res-1)