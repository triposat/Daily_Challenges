from heapq import heapify, heappop, heappush
from collections import defaultdict


class FreqStack:
    def __init__(self):
        self.heap = []
        heapify(self.heap)
        self.seen = defaultdict(int)
        self.count = 0

    def push(self, val: int) -> None:
        seen, maxHeap, count = self.seen, self.heap, self.count
        seen[val] += 1
        heappush(maxHeap, (-seen[val], -count, val))
        self.count += 1

    def pop(self) -> int:
        maxHeap = self.heap
        seen = self.seen
        rem = heappop(maxHeap)
        seen[rem[2]] -= 1
        return rem[2]

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
