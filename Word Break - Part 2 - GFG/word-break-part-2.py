class Solution:
   def wordBreak(self, n, dict, s):
       # code here
       wordset=set(dict)
       res=[]
       def word(ind=0,path=[]):
           if ind==len(s):
               res.append(" ".join(path))
           for j in range(ind+1,len(s)+1):
               words=s[ind:j]
               if words in wordset:
                   word(j,path+[words])
       word()
       return res

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        dict = input().split()
        s = input()
        
        ob = Solution()
        ans = ob.wordBreak(n, dict, s)
        if(len(ans) == 0):
            print("Empty")
        else:
            ans.sort()
            for it in (ans):
                print("("+it,end = ")")
            print()
# } Driver Code Ends