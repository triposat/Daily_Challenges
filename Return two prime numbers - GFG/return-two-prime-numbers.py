#User function Template for python3

class Solution:
    def primeDivision(self, n):
        def sieve(n):
            hey=[True for i in range(n+1)]
            hey[0]=False
            hey[1]=False
            p=2
            while (p*p<=n):
                if hey[p]==True:
                    for i in range(p*p, n+1, p):
                        hey[i]=False
                p+=1
            i=1
            j=n-1
            while i<=j:
                if hey[i] and hey[j]:
                    return [i, j]
                i+=1
                j-=1
        return sieve(n)

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        
        ob = Solution()
        p1, p2 = ob.primeDivision(N)
        print(p1,end=" ")
        print(p2)
# } Driver Code Ends