class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path = [c for c in path.split("/") if c != "." and c != ""]
        for c in path:
            if c == "..":
                if len(stack) > 0:
                    stack.pop()
            else:
                    stack.append(c)
        return "/"+"/".join(stack)