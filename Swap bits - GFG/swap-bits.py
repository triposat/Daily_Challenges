#User function Template for python3

class Solution:
    def swapBits(self, X, P1, P2, N):
            for i in range(0,N):
                temp1 = (1<<(P1+i))
                temp2 = (1<<(P2+i))
                if temp1 & X == temp2 & X  or (temp1 & X == temp1 and temp2 & X == temp2):
                    continue
                else:
                    X ^= temp2
                    X ^= temp1
            return X

#{ 
#  Driver Code Starts

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        obj = Solution()
        X, P1, P2, N = map(int, input().split())
        print(obj.swapBits(X, P1, P2, N))
        

# } Driver Code Ends