# # Recursion
# # Time: (2^n)
# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#         def helper(s):
#             if not s:
#                 return True
#             for word in wordDict:
#                 if word == s[0:len(word)]:
#                     if helper(s[len(word):]):
#                         return True
#             return False
#         return helper(s)
    
# # Recursion: Very Optimal then the above code
# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#         @cache
#         def helper(s):
#             if not s:
#                 return True
#             for word in wordDict:
#                 if word == s[0:len(word)]:
#                     if helper(s[len(word):]):
#                         return True
#             return False
#         return helper(s)
    
# DP
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        dp = [0]*len(s)
        for i in range(len(dp)):
            for j in range(i+1):
                w2Check = s[j:i+1]
                if w2Check in wordDict:
                    if j == 0:
                        dp[i] += 1
                    else:
                        dp[i] += dp[j-1]
        return dp[len(s)-1]>0