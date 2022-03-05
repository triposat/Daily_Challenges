class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        
        def helper(num):
            t=''
            for c in str(num):
                i=int(c)
                t+=str(mapping[i])
            t=int(t)
            return t
                
        temp=[]
        for i,num in enumerate(nums):
            temp.append([helper(num),i])
        temp.sort()
        t=[]
        for a,b in temp:
            t.append(nums[b])
        return t