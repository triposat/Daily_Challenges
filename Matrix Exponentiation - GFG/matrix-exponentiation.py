class Solution:
    def FindNthTerm(self, n):
        m = (10**9)+7
        def multi(mat, ans):
            res = [[0, 0], [0, 0]]
            for i in range(len(mat)):
                for j in range(len(ans)):
                    for k in range(len(mat)):
                        res[i][j] += (mat[i][k]%m)*(ans[k][j]%m)
            return res

        mat = [[1, 1], [1, 0]]
        ans = [[1, 1], [1, 0]]
        while n:
            if n & 1:
                ans = multi(mat, ans)
                n -= 1
            else:
                mat = multi(mat, mat)
                n >>= 1
        return ans[0][1]%m
	    
	    
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