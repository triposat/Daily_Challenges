class Solution:
    def canMakeTriangle(self, A, N):
        n = len(A)
        arr = [None]*(n-2)
        for i in range(n-2):
            if A[i]+A[i+1] > A[i+2] and A[i]+A[i+2] > A[i+1] and A[i+1]+A[i+2] > A[i]:
                arr[i] = 1
            else:
                arr[i] = 0
        return arr


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input())
        A = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.canMakeTriangle(A, N)
        for i in ans:
            print(i,end=" ")
        print()

# } Driver Code Ends