class Solution:
    def smallestSubstring(self, S):
        pos=[-333333]*3
        ans=99999
        for i, ch in enumerate(S):
            pos[int(ch)]=i
            # print(pos)
            ans=min(ans,max(pos)-min(pos)+1)
            # print(pos, ans)
        return -1 if ans==99999 else ans
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	t=int(input())
	for i in range(t):
		S = input()
		ob = Solution()
		ans = ob.smallestSubstring(S)
		
		print(ans)



# } Driver Code Ends