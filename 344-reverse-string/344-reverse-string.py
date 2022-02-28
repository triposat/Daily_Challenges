# Iterative Approach
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)//2
        for i in range(n):
            s[i], s[-(i+1)] = s[-(i+1)], s[i]

# Recursive Approach
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def revStr(st, s, e):
            if s >= e:
                return
            st[s], st[e] = st[e], st[s]
            revStr(st, s+1, e-1)

        revStr(s, 0, len(s)-1)