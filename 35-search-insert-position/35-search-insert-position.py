class Solution:
    def searchInsert(self, nums: List[int], tar: int) -> int:
        st=0
        end=len(nums)
        while st<end:
            mid=(st+end)>>1
            if nums[mid]==tar:
                return mid
            elif nums[mid]<tar:
                st=mid+1
            else:
                end=mid
        return st