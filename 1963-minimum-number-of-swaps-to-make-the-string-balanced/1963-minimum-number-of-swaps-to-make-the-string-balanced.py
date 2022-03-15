class Solution:
    def minSwaps(self, s: str) -> int:
        # Space: O(n)
        mism = 0
        stack = []
        for i in s:
            if i == '[':
                stack.append(i)
            else:
                if stack:
                    stack.pop()
                else:
                    mism += 1
        return (mism+1)//2
        # Space: O(1)
        stack = 0
        for i in s:
            if i == '[':
                stack += 1
            else:
                if stack > 0:
                    stack -= 1
        return (stack+1)//2
