from collections import defaultdict
class Solution:
    def checkMirrorTree(self, n, e, A, B):
        # code here
        hey1=defaultdict(list)
        hey2=defaultdict(list)
        for i in range(0, 2*e, 2):
            hey1[A[i]].append(A[i+1])
            hey2[B[i]].append(B[i+1])
        for me in hey1:
            if hey1[me]!=list(reversed(hey2[me])):
                return 0
        return 1

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n,e=map(int,input().split())
        
        A=list(map(int,input().split()))
        B=list(map(int,input().split()))
        
        ob = Solution()
        print(ob.checkMirrorTree(n,e,A,B))
# } Driver Code Ends