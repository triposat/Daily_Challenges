from collections import defaultdict
class Solution:
    def findHeight(self, N, arr):
        x=arr[N-1]
        h=1
        while x!=-1:
            x=arr[x]
            h+=1
        return h

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for i in range(N):
            arr[i] = int(arr[i])
        
        ob = Solution()
        print(ob.findHeight(N, arr))
# } Driver Code Ends