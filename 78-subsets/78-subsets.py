class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[[]]
        for num in nums:
            res+=[curr+[num] for curr in res]
        return res
        # outer=[]
        # outer.append([])
        # for num in nums:
        #     n=len(outer)
        #     for i in range(n):
        #         inner = outer[i][:]
        #         inner.append(num)
        #         outer.append(inner)
        # return outer