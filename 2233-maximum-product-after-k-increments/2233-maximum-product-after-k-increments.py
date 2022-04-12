class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        heapify(nums)
        for _ in range(k):
            heappush(nums, heappop(nums)+1)
        ans=1
        while nums:
            ans = (ans*heappop(nums))%(10**9+7)
        return ans