from heapq import heappush, heappop, heapify


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k==1:
            return nums
        maxHeap = []
        heapify(maxHeap)
        for i in range(k):
            heappush(maxHeap, (-nums[i], i))
        res = [-maxHeap[0][0]]
        for wE in range(k, len(nums)):
            while maxHeap[0][1] <= wE-k:
                heappop(maxHeap)
            heappush(maxHeap, (-nums[wE], wE))
            res.append(-maxHeap[0][0])
        return res