class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [['$', 1]]
        for ele in s:
            if ele == stack[-1][0]:
                stack[-1][1] += 1
            else:
                stack.append([ele, 1])
            while stack[-1][1] >= k:
                stack[-1][1] -= k
                if stack[-1][1] == 0:
                    stack.pop()
        return "".join(ele*freq for ele, freq in stack[1:])