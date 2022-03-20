class Solution:
    def minDominoRotations(self, A, B):
        s, n = set([1,2,3,4,5,6]), len(A)
        s = set([A[0], B[0]])
        for i in range(1, n): 
            s &= set([A[i], B[i]])
            # print(s)
        if not s: return -1
        flips1 = sum(A[i] == list(s)[0] for i in range(n))
        flips2 = sum(B[i] == list(s)[0] for i in range(n))
        return min(n - flips1, n - flips2) 
    
# 3 5 1 2 3
# 3 6 3 3 4

# 2 1 2 4 2 2
# 5 2 6 2 3 2