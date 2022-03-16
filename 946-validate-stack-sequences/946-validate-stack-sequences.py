class Solution:
    def validateStackSequences(self, pu: List[int], po: List[int]) -> bool:
        stack=[]
        i=0
        for ele in pu:
            stack.append(ele)
            while stack and stack[-1]==po[i]:
                i+=1
                stack.pop()
        return i==len(po)