class Solution:
    def solve(self, q, n):
        toad = q-1
        leng = n//2
        if n%2==0:
            hey = int(('1'+'0'*(leng-1)))
            le=len(str(hey))
            hey+=toad
            if len(str(hey))>le:
                return -1
            me =str(hey)
            me+=me[::-1]
            return int(me)
        else:
            hey = int(('1'+'0'*(leng)))
            le=len(str(hey))
            hey+=toad
            if len(str(hey))>le:
                return -1
            hey=str(hey)
            me =str(hey)[:-1]
            hey+=me[::-1]
            return int(hey)
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        res=[]
        for q in queries:
            res.append(self.solve(q, intLength))
        return res