class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = [['$', 1]]
        for ele in s:
            if ele == stack[-1][0]:
                stack[-1][1] += 1
            else:
                stack.append([ele, 1])
            if stack[-1][1] > 1:
                    stack.pop()
        return "".join(ele*freq for ele, freq in stack[1:])