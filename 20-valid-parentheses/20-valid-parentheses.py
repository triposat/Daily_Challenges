class Solution:
    def isValid(self, s: str) -> bool:
        par = {"}": "{", ")": "(", "]": "["}
        stack = []
        for char in s:
            if char in par.values():
                stack.append(char)
            elif char in par.keys():
                if stack == [] or par[char] != stack.pop():
                    return False
            else:
                return False
        return stack == []