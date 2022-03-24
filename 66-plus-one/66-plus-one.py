class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        d = int("".join(map(str, digits)))
        ans = list(str(d+1))
        return ans