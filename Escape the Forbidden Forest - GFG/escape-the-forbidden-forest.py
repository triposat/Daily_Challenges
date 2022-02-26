class Solution:
    def lcs(self, i, j, m, n, s1, s2, dp):
        if i == m or j == n:
            return 0
        if dp[i][j] != -1:
            return dp[i][j]
        elif s1[i] == s2[j]:
            dp[i][j] = 1+self.lcs(i+1, j+1, m, n, s1, s2, dp)
            return dp[i][j]
        else:
            dp[i][j] = max(self.lcs(i+1, j, m, n, s1, s2, dp),
                           self.lcs(i, j+1, m, n, s1, s2, dp))
            return dp[i][j]

    def build_bridges(self, s1, s2):
        m = len(s1)
        n = len(s2)
        dp = [[-1 for _ in range(n+1)] for _ in range(m+1)]
        return self.lcs(0, 0, m, n, s1, s2, dp)
        


#{ 
#  Driver Code Starts
if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        obj = Solution()
        str1, str2 = input().split()
        print(obj.build_bridges(str1, str2))

# } Driver Code Ends