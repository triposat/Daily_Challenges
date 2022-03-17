class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        seen = {}
        ans = -1
        for ind, val in enumerate(s):
            if val in seen:
                ans = max(ans, ind-seen[val]-1)
            seen.setdefault(val, ind)
        return ans
