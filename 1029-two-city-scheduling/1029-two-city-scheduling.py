class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        add = 0
        res = []
        for i, j in costs:
            add += i
            res.append(j-i)
        res.sort()
        for i in range(len(costs)//2):
            add += res[i]
        return add