class Solution:
    def chooseandswap (self, A):
       # code here
       l = len(A)
       covered = set()
       for i in range(l):
           smaller = A[i]
           covered.add(smaller)
           for j in A[i+1:]:
               if j<smaller and j not in covered:
                   smaller = j
           if smaller != A[i]:
               break
       if smaller == A[i]:
           return A
       temp = A[i]
       res = ""
       for j in range(l):
           flag = True
           if temp == A[j]:
               flag = False
               res += smaller
           elif flag and A[j] == smaller:
               res += temp
           else:
               res+=A[j]
       return res




#{ 
#  Driver Code Starts
#Initial Template for Python 3




if __name__ == '__main__': 
    ob = Solution()
    t = int (input ())
    for _ in range (t):
        A = input()
        ans = ob.chooseandswap(A)
        print(ans)


# } Driver Code Ends