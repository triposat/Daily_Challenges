from collections import Counter
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s = Counter(s)
        cnt = 0
        for c in t:
            if s[c] > 0:
                s[c] -= 1
            else:
                cnt += 1
        return cnt
