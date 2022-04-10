from heapq import heapify, heappop, heappush
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hMap = Counter(nums)
        maxHeap = []
        heapify(maxHeap)
        for i, j in hMap.items():
            heappush(maxHeap, (-j, i))
        res = []
        for i in range(k):
            res.append(heappop(maxHeap)[1])
        return res