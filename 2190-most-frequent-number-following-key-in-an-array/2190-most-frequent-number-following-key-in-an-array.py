from collections import Counter
class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        hashMap = Counter(nums)
        cnt = 0
        for i in range(len(nums)-1):
            if nums[i] == key:
                if hashMap[nums[i+1]] > cnt:
                    cnt = hashMap[nums[i+1]]
                    res = nums[i+1]
        return res