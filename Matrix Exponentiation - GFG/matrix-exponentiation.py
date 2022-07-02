class Solution:
    def FindNthTerm(self, n):
        m = (10**9)+7
        def multi(m1, m2):
            res = [[0, 0], [0, 0]]
            for i in range(len(m1)):
                for j in range(len(m2)):
                    for k in range(len(m1)):
                        res[i][j] += (m1[i][k]%m)*(m2[k][j]%m)
            return res
        m1 = [[1, 1], [1, 0]]
        m2 = [[1, 1], [1, 0]]
        while n:
            if n & 1:
                m2 = multi(m1, m2)
                n -= 1
            else:
                m1 = multi(m1, m1)
                n >>= 1
        return m2[0][1]%m
	    
	    
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