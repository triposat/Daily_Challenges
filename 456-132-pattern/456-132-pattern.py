# Time: O(n^3)
# class Solution:
#     def find132pattern(self, nums: List[int]) -> bool:
#         n = len(nums)
#         if n < 3:
#             return False
#         for i in range(n):
#             for j in range(i+1, n):
#                 for k in range(j+1, n):
#                     if nums[i] < nums[k] and nums[k] < nums[j]:
#                         return True
#         return False
    
# Time: O(n^2)
# class Solution:
#     def find132pattern(self, nums: List[int]) -> bool:
#         n = len(nums)
#         if n < 3:
#             return False
#         mi = nums[0]
#         for j in range(1, n-1):
#             for k in range(j+1, n):
#                 if mi < nums[k] and nums[k] < nums[j]:
#                     return True
#             mi = min(mi, nums[j])
#         return False

# Time: O(n)
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False
        k = -(1 << 31)
        st = []
        for i in range(n)[::-1]:
            if nums[i] < k:
                return True
            else:
                while st and nums[i] > st[-1]:
                    k = st.pop()
            st.append(nums[i])
        return False