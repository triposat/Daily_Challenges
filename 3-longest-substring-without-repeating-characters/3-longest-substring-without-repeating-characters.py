class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans=""
        res=0
        ws=0
        for i in range(len(s)):
            ans+=s[i]
            while len(ans)!=len(set(ans)):
                ans=ans[1:]
                ws+=1
            res=max(res, i-ws+1)
        return res
    