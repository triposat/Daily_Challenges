class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        hey=Counter(nums)
        cnt=0
        for i in range(len(nums)-1):
            if nums[i]==key:
                if hey[nums[i+1]]>cnt:
                    cnt = hey[nums[i+1]]
                    ans = nums[i+1]
        return ans
                