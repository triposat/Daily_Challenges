class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        hey=[]
        heapify(hey)
        for ele in stones:
            heappush(hey, -ele)
        while len(hey)>1:
            x = -1*heappop(hey)
            y = -1*heappop(hey)
            if x!=y:
                heappush(hey, -1*(x-y))
        if hey:
            return hey[0]*-1
        else:
            return 0