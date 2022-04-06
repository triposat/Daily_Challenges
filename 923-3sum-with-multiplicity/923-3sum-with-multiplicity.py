class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        mod = 10**9+7
        def twoSum(idx, tar):
            ans = 0
            hMap = defaultdict(lambda: 0)
            for i in range(idx, len(arr)):
                ele = tar-arr[i]
                ans += hMap[ele]
                hMap[arr[i]] += 1
            return ans
        ans = 0
        for idx, val in enumerate(arr):
            ans += twoSum(idx+1, target-val)
        return ans % mod