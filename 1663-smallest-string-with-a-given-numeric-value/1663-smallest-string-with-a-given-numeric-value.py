class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        res = ['a']*n
        k -= n
        while k:
            res[n-1] = chr(97+min(25, k))
            k -= min(25, k)
            n -= 1
        return "".join(res)