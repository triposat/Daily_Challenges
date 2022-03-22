class Solution:
    def countCollisions(self, d: str) -> int:
        colli = []
        i = 0
        while i < len(d):
            cnt = 1
            while i+1 < len(d) and d[i] == d[i+1]:
                cnt += 1
                i += 1
            colli.append((cnt, d[i]))
            i += 1
        ans = 0
        for i in range(len(colli)-1):
            if colli[i][1] == "R" and colli[i+1][1] == "L":
                ans += colli[i][0]+colli[i+1][0]
            elif colli[i][1] == "R" and colli[i+1][1] == "S":
                ans += colli[i][0]
            elif colli[i][1] == "S" and colli[i+1][1] == "L":
                ans += colli[i+1][0]
        return ans