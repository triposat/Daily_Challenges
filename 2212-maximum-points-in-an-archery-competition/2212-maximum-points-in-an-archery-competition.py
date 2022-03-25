class Solution:
    def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:
        score = 0
        res = 0
        for i in range(1 << 12):
            arrow = numArrows
            temp = [0]*12
            for j in range(12)[::-1]:
                if i & (1 << j):
                    if arrow <= aliceArrows[j]:
                        continue
                    arrow -= aliceArrows[j]+1
                    temp[j] = aliceArrows[j]+1
            temp[0]+=arrow
            bob = 0
            for j in range(12):
                if temp[j] > aliceArrows[j]:
                    bob += j
            if bob > score:
                score = bob
                res = temp
        return res