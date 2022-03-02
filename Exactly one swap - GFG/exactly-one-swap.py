from collections import Counter
#User function Template for python3
class Solution:
    def countStrings(self, S): 
        n=len(S)
        if len(set(S))==len(S):
            return n*(n-1)//2
        S=Counter(S)
        S=list(S.values())
        res=0
        for i in range(len(S)):
            res+=S[i]*sum(S[i+1:])
        return res+1

#{ 
#  Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        S = input()
        ob = Solution()
        ans = ob.countStrings(S)
        print(ans)
# } Driver Code Ends