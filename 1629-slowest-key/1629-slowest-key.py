class Solution:
    def slowestKey(self, rt: List[int], kp: str) -> str:
        beginT = rt[0]
        beginK = kp[0]
        for i in range(1, len(rt)):
            diff = rt[i]-rt[i-1]
            if diff > beginT or (diff == beginT and ord(kp[i]) > ord(beginK)):
                beginT = diff
                beginK = kp[i]
        return beginK