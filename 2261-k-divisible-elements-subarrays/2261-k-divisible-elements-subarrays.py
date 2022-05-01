class Solution:
    def countDistinct(self, A: List[int], k: int, p: int) -> int:
        subA = [tuple(A[i:j]) for i in range(0, len(A))
                for j in range(i + 1, len(A) + 1)]
        subA = set(subA)
        res = []
        for i in subA:
            cnt = 0
            for j in i:
                if j % p == 0:
                    cnt += 1
            if cnt <= k:
                res.append(i)
        return len(res)