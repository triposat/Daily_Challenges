class Solution:
    def solve(self, q, n):
        toAdd = q-1
        leng = n//2
        if n % 2 == 0:
            half = int(('1'+'0'*(leng-1)))
            hafL = len(str(half))
            half += toAdd
            if len(str(half)) > hafL:
                return -1
            full = str(half)
            full += full[::-1]
            return int(full)
        else:
            half = int(('1'+'0'*(leng)))
            hafL = len(str(half))
            half += toAdd
            if len(str(half)) > hafL:
                return -1
            half = str(half)
            full = str(half)[:-1]
            half += full[::-1]
            return int(half)

    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        res = []
        for q in queries:
            res.append(self.solve(q, intLength))
        return res