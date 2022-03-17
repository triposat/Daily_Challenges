class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        ans = 0
        for brac in s:
            val = 0
            if brac == "(":
                stack.append(0)
            else:
                while stack[-1] != 0:
                    val += stack.pop()
                val = max(2*val, 1)
                stack.pop()
                stack.append(val)
        while stack:
            ans += stack.pop()
        return ans