class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        hashm = {}
        ans = 1e9
        for idx, val in enumerate(cards):
            if val in hashm:
                ans = min(ans, idx-hashm[val]+1)
            hashm[val] = idx
        return ans if ans != 1e9 else -1
