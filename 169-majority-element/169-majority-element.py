class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = 0
        cur = 0
        for ele in nums:
            if cnt == 0:
                cur = ele
            if cur == ele:
                cnt += 1
            else:
                cnt -= 1
        return cur