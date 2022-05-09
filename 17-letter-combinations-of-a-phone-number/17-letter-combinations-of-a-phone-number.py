class Solution:
    def letterCombinations(self, d: str) -> List[str]:
        if d=="":
            return []
        comb = [0, 1, 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        res=[]
        d = list(d)
        def ans(idx, me):
            if idx==len(d):
                res.append(me)
                return
            dig = d[idx]
            for i in list(comb[int(dig)]):
                ans(idx+1, me+i)
            
        ans(0, "")
        return res
        
        