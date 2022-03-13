class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        hMap = Counter(nums)
        hMap = sorted(hMap)
        start = 1
        ans = 0
        for key in hMap:
            gap = key-start
            s = start
            e = key
            if k >= gap:
                k -= gap
            else:
                break
            ans += e*(e-1)//2 - s*(s-1)//2
            start = e+1
        s = start
        e = start+k
        ans += e*(e-1)//2 - s*(s-1)//2
        return ans