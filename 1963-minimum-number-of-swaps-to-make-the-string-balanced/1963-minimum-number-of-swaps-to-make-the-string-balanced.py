class Solution:
    def minSwaps(self, s: str) -> int:
        mism=0
        stack=[]
        for i in s:
            if i=='[':
                stack.append(i)
            else:
                if stack:
                    stack.pop()
                else:
                    mism+=1
        return (mism+1)//2