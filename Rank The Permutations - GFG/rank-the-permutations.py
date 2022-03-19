class Solution:
    def facto(self, n):
        if n == 0:
            return 1
        return n * self.facto(n-1)

    def findRank(self, S):
        n = len(S)
        ans = 0
        for i in range(n):
            cnt = 0
            for j in range(i+1, n):
                if S[j] < S[i]:
                    cnt += 1
            ans += cnt*self.facto(n-i-1)
        return ans+1

#{ 
#  Driver Code Starts
#Initial Template for Python 3
		
if __name__ == '__main__':
    T=int(input())
    for i in range(T):
    	str = input().strip()
    	obj = Solution()
    	ans = obj.findRank(str)
    	print(ans)
# } Driver Code Ends