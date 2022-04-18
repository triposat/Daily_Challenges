class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        x = 0
        res = 0
        while True:
            y = total-cost1*x
            x += 1
            if y < 0:
                break
            res += (y//cost2)+1
        return res