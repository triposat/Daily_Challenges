class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def solve(nums, left, right, tar):
            if right > left:
                mid = (left+right) >> 1
                if nums[mid] == tar:
                    return mid
                elif nums[mid] < tar:
                    return solve(nums, mid+1, right, tar)
                else:
                    return solve(nums, left, mid, tar)
            return -1

        return solve(nums, 0, len(nums), target)