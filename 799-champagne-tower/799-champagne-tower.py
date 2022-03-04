class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        # res=[[0]*i for i in range(1, 102)]
        # res[0][0]=poured
        # for i in range(query_row+1):
        #     for j in range(i+1):
        #         Q=(res[i][j]-1)/2
        #         if Q>0:
        #             res[i+1][j]+=Q
        #             res[i+1][j+1]+=Q
        # return min(1, res[query_row][query_glass])
        hey=[poured]
        
        for _ in range(query_row):
            me=[0]*(len(hey)+1)
            for j in range(len(hey)):
                Q=(hey[j]-1)/2
                if Q>0:
                    me[j]+=Q
                    me[j+1]+=Q    
            hey=me
        return min(1, hey[query_glass])