class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        if n <= 1:
            return

        # 1st Step...
        i = n-2
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        # ...

        if i < 0:
            # It shows that all the elements are in descending order.
            nums[:] = nums[::-1]
        else:
            # 2nd Step...
            j = n-1
            while nums[j] <= nums[i]:
                j -= 1
            # ...

            # 3rd Step...
            nums[i], nums[j] = nums[j], nums[i]
            # ...

            # 4th Step...
            nums[i+1:] = sorted(nums[i+1:])
            # ...