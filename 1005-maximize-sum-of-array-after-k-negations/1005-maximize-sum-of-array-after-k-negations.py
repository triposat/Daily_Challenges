from heapq import heappop, heappush, heapify
class Solution:
    def largestSumAfterKNegations(self, A, k):
        heapify(A)
        while k > 0:
            k -= 1
            heappush(A, -heappop(A))
        return sum(A)