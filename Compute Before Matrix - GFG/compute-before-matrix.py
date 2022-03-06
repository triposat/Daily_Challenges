class Solution:
    def computeBeforeMatrix(self, n, m, after):
        res = [[0]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    res[0][0] = after[0][0]
                elif i == 0:
                    res[i][j] = after[i][j]-after[i][j-1]
                elif j == 0:
                    res[i][j] = after[i][j]-after[i-1][j]
                else:
                    res[i][j] = after[i][j]+after[i-1][j-1] - \
                        after[i-1][j]-after[i][j-1]
        return res

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    
    T = int(input())
    while T > 0: 
        N, M =[int(i) for i in input().split()]
        after= []
        for j in range (N):
            after.append([int(i) for i in input().split()])
        ob = Solution()
        before=ob.computeBeforeMatrix(N,M,after)
        for i in range(len(before)): 
            for j in range(len(before[i])):
                print(before[i][j],end=' ')
            print()
        
        
        T -= 1
# } Driver Code Ends