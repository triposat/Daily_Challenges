# Time: O(m+n)
# Space: O(m+n)
# class Solution:
#     def backspaceCompare(self, s: str, t: str) -> bool:
#         def stack(string):
#             res = []
#             for var in string:
#                 if var != "#":
#                     res.append(var)
#                 else:
#                     if not res:
#                         continue
#                     res.pop()
#             return res
#         s = stack(s)
#         t = stack(t)
#         return s == t
# Time: (m+n)
# Space: O(1)
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s=list(s)
        t=list(t)
        k = 0
        for i in range(len(s)):
            if s[i] != '#':
                s[k] = s[i]
                k += 1
            else:
                k -= 1
                k = max(0, k)
        l = 0
        for i in range(len(t)):
            if t[i] != '#':
                t[l] = t[i]
                l += 1
            else:
                l -= 1
                l = max(0, l)
        if k != l:
            return False
        else:
            for i in range(k):
                if s[i] != t[i]:
                    return False
            return True
                