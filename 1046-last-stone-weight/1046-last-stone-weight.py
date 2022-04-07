from heapq import heappop, heappush, heapify
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        ans = []
        heapify(ans)
        for ele in stones:
            heappush(ans, -ele)
        while len(ans) > 1:
            x = -1*heappop(ans)
            y = -1*heappop(ans)
            if x != y:
                heappush(ans, -1*(x-y))
        if ans:
            return ans[0]*-1
        else:
            return 0