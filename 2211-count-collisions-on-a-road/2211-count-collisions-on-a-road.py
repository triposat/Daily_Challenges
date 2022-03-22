class Solution:
    def countCollisions(self, directions: str) -> int:
        # 1st Approach
        colli = []
        i = 0
        while i < len(directions):
            cnt = 1
            while i+1 < len(directions) and directions[i] == directions[i+1]:
                cnt += 1
                i += 1
            colli.append((cnt, directions[i]))
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
        
        # 2nd Approach
        ans = 0
        temp = 0
        for dire in directions:
            if dire == "L":
                ans += temp
            else:
                temp = 1
        temp = 0
        for dire in directions[::-1]:
            if dire == "R":
                ans += temp
            else:
                temp = 1
        return ans