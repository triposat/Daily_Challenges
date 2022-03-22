class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        n = len(tops)
        s = set([tops[0], bottoms[0]])
        for i in range(1, n):
            s &= set([tops[i], bottoms[i]])
        if not s:
            return -1
        flipsA = sum(tops[i] == list(s)[0] for i in range(n))
        flipsB = sum(bottoms[i] == list(s)[0] for i in range(n))
        return min(n-flipsA, n-flipsB)