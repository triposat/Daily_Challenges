# Time : O(nlogn)
# class Solution:
#     def maxOperations(self, nums: List[int], k: int) -> int:
#         nums.sort()
#         left = 0
#         right = len(nums)-1
#         cnt = 0
#         while left < right:
#             ans = nums[left]+nums[right]
#             if ans < k:
#                 left += 1
#             elif ans > k:
#                 right -= 1
#             else:
#                 cnt += 1
#                 left += 1
#                 right -= 1
#         return cnt

# Time: O(n)
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        hmap = defaultdict(int)
        ans = 0
        for val in nums:
            rem = k-val
            if hmap[val] > 0:
                ans += 1
                hmap[val] -= 1
            else:
                hmap[rem] += 1
        return ans