class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        res = {0: 1}
        count = 0
        totSum = 0
        for ele in nums:
            totSum = (totSum+ele) % k
            if totSum < 0:
                totSum += k
            if totSum in res:
                count += res[totSum]
            if totSum not in res:
                res[totSum] = 0
            res[totSum] += 1
        return count