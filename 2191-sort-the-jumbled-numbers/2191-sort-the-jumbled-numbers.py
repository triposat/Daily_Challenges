class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            ans = ""
            for char in str(num):
                ans += str(mapping[int(char)])
            res.append(int(ans))
        final = list(zip(nums, res))
        final = sorted(final, key=lambda x: x[1])
        return [tup[0] for tup in final]