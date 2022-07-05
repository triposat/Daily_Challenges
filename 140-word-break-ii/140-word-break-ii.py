# DP
# Time Complexity: O(n^3)
# class Solution:
#     def helper(self, s, words, dp):
#         if s in dp:
#             return dp[s]
#         if not s:
#             return []
#         res = []
#         for word in words:
#             if not s.startswith(word):
#                 continue
#             if len(word) == len(s):
#                 res.append(word)
#             else:
#                 rest = self.helper(s[len(word):], words, dp)
#                 for item in rest:
#                     ans = word + ' ' + item
#                     res.append(ans)
                    
#         dp[s] = res
#         return res

#     def wordBreak(self, s: str, words: List[str]) -> List[str]:
#         return self.helper(s, words, {})



class Solution:
    def helper(self, s, words, dp):
        res = []
        for word in words:
            if not s.startswith(word):
                continue
            if len(word) == len(s):
                res.append(word)
            else:
                rest = self.helper(s[len(word):], words, dp)
                for item in rest:
                    ans = word + ' ' + item
                    res.append(ans)
        return res

    def wordBreak(self, s: str, words: List[str]) -> List[str]:
        return self.helper(s, words, {})