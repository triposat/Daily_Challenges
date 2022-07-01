from typing import List
class Solution:
    def matrixMultiplication(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        MOD = 1000000007
        dim = len(mat1)
        res = [[0]*dim for _ in range(dim)]

        for i in range(dim):
            for j in range(dim):
                for k in range(dim):
                    res[i][j] = (res[i][j] + ((mat1[i][k] % MOD) * (mat2[k][j] % MOD) % MOD)) % MOD 
        
        return res

    def getIdentityMatrix(self, dim):
        res = [[0]*dim for _ in range(dim)]
        for i in range(dim):
            res[i][i] = 1
        
        return res

    def matrixExpo(self, matrix: List[List[int]], power: int) -> List[List[int]]:
        dim = len(matrix)
        result = self.getIdentityMatrix(dim)

        while power > 0:
            if power & 1:
                result = self.matrixMultiplication(result, matrix)
                power -= 1
            else:
                matrix = self.matrixMultiplication(matrix, matrix)
                power = power >> 1
        
        return result
        
    def FindNthTerm(self, n):
        if n == 0:
            return 0

        mat = self.matrixExpo([[0, 1], [1, 1]], n)
        return mat[1][1]

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution()
		ans = ob.FindNthTerm(n)
		print(ans)

# } Driver Code Ends