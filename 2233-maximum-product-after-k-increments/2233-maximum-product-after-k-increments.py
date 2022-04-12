class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        heapify(nums)
        for _ in range(k):
            heappush(nums, heappop(nums)+1)
        # print(nums)
        ans=1
        while nums:
            ans*=heappop(nums)
            ans = ans%(10**9+7)
        return ans