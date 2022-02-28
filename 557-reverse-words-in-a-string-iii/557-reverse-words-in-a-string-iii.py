class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        res = []
        for word in s:
            word = word[::-1]
            res.append(word)
        return " ".join(res)