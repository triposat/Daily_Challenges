class Solution:
    def smallestSubstring(self, S):
        res = [-1, -1, -1]
        maxi = (1 << 31)
        if not S.count("0") or not S.count("1") or not S.count("2"):
            return -1
        for idx, val in enumerate(S):
            res[int(val)] = idx
            if -1 not in res:
                maxi = min(maxi, max(res)-min(res))
        return maxi+1
        
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