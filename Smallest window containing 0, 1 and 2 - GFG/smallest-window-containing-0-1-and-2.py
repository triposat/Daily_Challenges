class Solution:
    def smallestSubstring(self, S):
        pos=[-333333]*3
        ans=99999
        if not S.count("0") or not S.count("1") or not S.count("2"):
            return -1
        for i, ch in enumerate(S):
            pos[int(ch)]=i
            ans=min(ans,max(pos)-min(pos)+1)
        return ans
        

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