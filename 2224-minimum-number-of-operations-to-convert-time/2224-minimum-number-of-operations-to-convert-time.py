class Solution:
    def convertTime(self, cur: str, cor: str) -> int:
        x, y = map(int, cur.split(":"))
        p, q = map(int, cor.split(":"))
        x = x*60+y
        p = p*60+q
        ans = 0
        diff = p-x
        for i in [60, 15, 5, 1]:
            ans += diff//i
            diff = diff % i
        return ans