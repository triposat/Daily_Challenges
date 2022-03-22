class Solution:
    def minRepeats(self, A, B):
        diff = len(B)//len(A)
        if B in A*diff:
            return diff
        if B in A*(diff+1):
            return diff+1
        if B in A*(diff+2):
            return (diff+2)
        return -1

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        A=input()
        B=input()
        
        ob = Solution()
        print(ob.minRepeats(A,B))
# } Driver Code Ends