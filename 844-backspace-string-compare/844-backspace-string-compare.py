class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def stack(string):
            res=[]
            for var in string:
                if var!="#":
                    res.append(var)
                else:
                    if not res:
                        continue
                    res.pop()
            return res
        s=stack(s)
        t=stack(t)
        return s==t