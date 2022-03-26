class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals = sorted(intervals, key=lambda x: x[0])
        for inter in intervals:
            if res and inter[0]<=res[-1][1]:
                res[-1][1] = max(res[-1][1], inter[1])
            else:
                res += [inter]
        return res