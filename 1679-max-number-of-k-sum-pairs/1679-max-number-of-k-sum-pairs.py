class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # 1 3 3 3 4
        nums.sort()
        i=0
        j=len(nums)-1
        cnt=0
        while i<j:
            ans = nums[i]+nums[j]
            if ans<k:
                i+=1
            elif ans>k:
                j-=1
            else:
                cnt+=1
                i+=1
                j-=1
        return cnt