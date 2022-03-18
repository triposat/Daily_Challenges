class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_occ = {val: idx for idx, val in enumerate(s)}
        stack = []
        visited = set()
        for idx, val in enumerate(s):
            if val in visited:
                continue
            while stack and val < stack[-1] and last_occ[stack[-1]] > idx:
                visited.remove(stack.pop())
            stack.append(val)
            visited.add(val)
        return "".join(stack)