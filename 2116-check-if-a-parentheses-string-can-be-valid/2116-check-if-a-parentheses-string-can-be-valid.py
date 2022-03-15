class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 != 0:
            return False
        # Forward Traverse
        brac = 0
        for i in range(len(s)):
            if s[i] == "(" or locked[i] == '0':
                brac += 1
            else:
                brac -= 1
            if brac < 0:
                return False
        # Backward Traverse
        brac = 0
        for i in range(len(s))[::-1]:
            if s[i] == ")" or locked[i] == '0':
                brac += 1
            else:
                brac -= 1
            if brac < 0:
                return False
        return True