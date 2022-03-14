from collections import Counter
class Solution:
    def biGraph(self, arr, n, e):
        if n==2 and e==1:
            return 1
        arr=Counter(arr)
        for i in arr:
            if arr[i]<2:
                return 0
        return 1
        
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n,e=map(int,input().split())
        arr=list(map(int,input().split()))
        
        ob = Solution()
        print(ob.biGraph(arr,n,e))
# } Driver Code Ends