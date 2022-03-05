from math import ceil
class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        n = len(s)
        rght = n-1
        ans = 0
        for left in range(ceil(n/2)):
            for j in range(rght, left-1, -1):
                if j == left:
                    ans += n//2-left
                elif s[left] == s[j]:
                    s = s[:j] + s[j+1:rght+1]+s[j]+s[rght+1:]
                    ans += rght-j
                    rght -= 1
                    break
        return ans