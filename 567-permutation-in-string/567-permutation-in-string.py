class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Len = len(s1)
        s2Len = len(s2)
        if s2Len < s1Len:
            return False
        s1Arr = [0]*26
        s2Arr = [0]*26
        left = 0
        right = 0
        while right < s1Len:
            s1Arr[ord(s1[right])-97] += 1
            s2Arr[ord(s2[right])-97] += 1
            right += 1
        right -= 1
        while right < s2Len:
            if s1Arr == s2Arr:
                return True
            right += 1
            if right != s2Len:
                s2Arr[ord(s2[right])-97] += 1
            else:
                break
            s2Arr[ord(s2[left])-97] -= 1
            left += 1
        return False