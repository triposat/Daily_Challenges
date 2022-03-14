class Solution:
    def digArtifacts(self, n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:
        dig = set((r, c) for r, c in dig)
        cnt = 0
        for r1, c1, r2, c2 in artifacts:
            pos = set()
            for r in range(r1, r2+1):
                for c in range(c1, c2+1):
                    pos.add((r, c))
            if all(p in dig for p in pos):
                cnt += 1
        return cnt