class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def solve(nums, st, end, tar):
            if end>st:
                mid=(st+end)>>1
                if nums[mid]==tar:
                    return mid
                elif nums[mid]<tar:
                    return solve(nums, mid+1, end, tar)
                else:
                    return solve(nums, st, mid, tar)
            return -1
    
        return solve(nums, 0, len(nums), target)