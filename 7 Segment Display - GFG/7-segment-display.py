#User function Template for python3

class Solution:
    def sevenSegments(self, S, N):
        arr=[6,2,5,5,4,5,6,3,7,5]
        sumi=0
        a=[6,2,5,5,4,5,6,3,7,5]
        for i in range(N):
            sumi+=a[int(S[i])]
        i=N
        ans=''
        while i>0:
            for j in range(10):
                if sumi-a[j]>=2*(i-1) and sumi-a[j]<=7*(i-1):
                    ans+=str(j)
                    sumi-=a[j]
                    break
            i-=1
        return ans

            
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        S=input()
        
        ob = Solution()
        print(ob.sevenSegments(S,N))
# } Driver Code Ends