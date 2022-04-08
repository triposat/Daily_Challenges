class Solution:
    def findWinners(self, nums: List[List[int]]) -> List[List[int]]:
        winers = [i[0] for i in nums]
        losers = [i[1] for i in nums]
        win = list(set(winers)-set(losers))
        lose = Counter(losers)
        ans = []
        for i in lose:
            if lose[i] == 1:
                ans.append(i)
        return [sorted(win), sorted(ans)]