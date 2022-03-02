class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        memo={}
        i=0
        j=0
        ans=0
        while j<len(s):
            memo[s[j]] = memo.get(s[j], 0)+1
            if len(memo)==j-i+1:
                ans = max(ans, j-i+1)
                j+=1
            else:
                if memo[s[i]]==1:
                    del memo[s[i]]
                    i+=1
                    j+=1
                else:
                    memo[s[i]]-=1
                    i+=1
                    j+=1
        return ans