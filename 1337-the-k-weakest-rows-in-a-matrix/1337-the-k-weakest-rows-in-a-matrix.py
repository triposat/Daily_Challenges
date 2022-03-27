# Approach 1:
# Time: O(mlogm) + O(m) + O(m) => O(mlogm)
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        temp = [arr.count(1) for arr in mat]  # O(m)
        print(temp)
        # O(mlogm) + O(m)
        res = [i[0] for i in sorted(enumerate(temp), key=lambda x:x[1])]
        print(res)
        return res[:k]

# Approach 2: Priority Queue
# Time: O(m)*(O(logn) + O(logk)) + O(klogk)
from heapq import heappushpop, heappush, heappop
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        heap = []  # Size: O(k)
        for idx, rows in enumerate(mat):  # O(m)
            sol_count = self.soldier_count(rows)
            if len(heap) == k:
                heappushpop(heap, (-sol_count, -idx))  # O(logk)
            else:
                heappush(heap, (-sol_count, -idx))  # O(logk)
        weak_heap = []  # Size: O(k)
        # O(klogk)
        while heap:
            weak_heap.append(-(heappop(heap)[1]))
        return weak_heap[::-1]

    # O(logn)
    def soldier_count(self, row: List[int]) -> int:
        low, high = 0, len(row)-1

        while low <= high:
            mid = low+(high-low) // 2

            if not row[mid]:
                high = mid - 1
            else:
                low = mid+1
        return low
