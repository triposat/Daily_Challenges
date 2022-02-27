class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s, t = Counter(s), Counter(t)
        sum=0
        for c in "abcdefghijklmnopqrstuvwxyz":
            sum+=abs(s[c]-t[c])
        return sum