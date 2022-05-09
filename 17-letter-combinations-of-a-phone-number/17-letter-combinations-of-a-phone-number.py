class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        comb = [0, 1, 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        res = []
        digits = list(digits)

        def dfs(idx, out):
            if idx == len(digits):
                res.append(out)
                return
            dig = digits[idx]
            for i in list(comb[int(dig)]):
                dfs(idx+1, out+i)
        dfs(0, "")
        return res