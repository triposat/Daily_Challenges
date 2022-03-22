class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        label = {val: idx for idx, val in enumerate(s)}
        l, r = 0, 0
        res = []
        for i in range(len(s)):
            r = max(r, label[s[i]])
            if i == r:
                res += [r-l+1]
                l = i+1
        return res